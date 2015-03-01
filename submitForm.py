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



