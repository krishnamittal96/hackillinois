import gdata.youtube
import gdata.youtube.service
import youtube_dl
import os
from subprocess import call
import sys

yt_service = gdata.youtube.service.YouTubeService()

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'relevance'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  temp=open("songdata.txt","w")
  temp.write(str(feed))
  temp.close()




songname=""
i=1
while i<len(sys.argv):
	if i == 1:
		songname = sys.argv[i]
	else:
		songname=songname+ ' ' +sys.argv[i]
	i=i+1

SearchAndPrint(songname) 

infile=open("songdata.txt","r")
while infile:
	line=infile.readline()
	if line.find("watch")>=0:
		n=line.find("watch")
		code=""
		count=1;
		while(line[n]!='&'):
			if count>=9 :
				code=code+line[n]
			n=n+1
			count=count+1
		break
infile.close()
os.remove("songdata.txt")
command="youtube-dl --extract-audio --audio-format mp3 -g http://www.youtube.com/watch?v="+code
temp=open("chrome.txt","w")
call(command.split(), shell=False,stdout=temp)
#temp=open("filename.txt","w")
#os.rename(code+".mp3",songname+".mp3")
#temp.write(songname+".mp3")
#temp.close()
