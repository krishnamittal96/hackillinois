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


import urllib
from subprocess import call
import sys
artistname=""
i=1
while i<len(sys.argv):
	if i == 1:
		artistname = sys.argv[i]
	else:
		artistname=artistname+ ' ' +sys.argv[i]
	i=i+1
f = urllib.urlopen("https://itunes.apple.com/search?term="+artistname+"&entity=musicArtist")
artistname = ''
i = 1
while i<len(sys.argv):
	if i == 1:
		artistname = sys.argv[i]
	else:
		artistname=artistname+ '_' +sys.argv[i]
	i=i+1
temp=open("data.txt","w")
temp.write(str(f.read()))
temp.close()
temp=open("data.txt","r")
while temp:
	line=temp.readline()
	if line.find("http")>=0:
		n=line.find("http")
		output=""
		while(line[n]!='?'):
			output=output+line[n]
			n=n+1
		break
temp.close()
temp=open("link.txt","w")
temp.write(output)

temp.close()
temp=open("data2.txt","w")
command="curl"+" "+output

cmd = command.split()
call(cmd,shell=False, stdout=temp)
temp.close()
temp=open("data2.txt","r")

data=temp.read()	
data = data.split('class="top-songs"')
temp.close()
temp = open("data3.txt","w")

data = data[1].split('preview-title="')
result = []
i=1
while (i<11):
	result.append(data[i].split('"')[0])
	i+=1
for song in result:
	temp.write(song)
	temp.write('\n')
print result
temp.close()


album=open("data3.txt","r")

counter=0
while(counter<10):
	song=album.readline()
	print song
	songname=song.split('\n')[0]
	songname=artistname+" "+songname
	

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
	print code
	print artistname
	command = "youtube-dl  "+code+" -x --audio-format mp3 -o "+artistname+"/%(title)s.(ext)s'"
	print command
	call(command.split(), shell=False)

	#os.rename(code+".mp3",songname+".mp3")

	counter=counter+1
		
