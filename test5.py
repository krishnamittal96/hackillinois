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
  name=str(feed)
  name=name.split("watch?v=")[1]
  name=name.split('&')[0]
  print name
  return name
  




songname=""
i=1
while i<len(sys.argv):
	if i == 1:
		songname = sys.argv[i]
	else:
		songname=songname+ ' ' +sys.argv[i]
	i=i+1

code=SearchAndPrint(songname) 
command = "youtube-dl  "+code+" -x --audio-format mp3 --audio-quality 1 -o %(id)s.(ext)s'"
call(command.split(), shell=False)
temp=open("filename.txt","w")
os.rename(code+".mp3",songname+".mp3")
temp.write(songname+".mp3")
temp.close()
