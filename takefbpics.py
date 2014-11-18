from urllib2 import urlopen
import os
import threading

if not os.path.exists("pics"):
    os.makedirs("pics")

f= open("pics.txt")
links = f.read()
f.close()
links = eval(links)


def storePic(name,link):
	f = open("pics/"+name,"wb")
	f.write(urlopen(link).read())
	f.close()

c = 0
for i in links:
	try:
		threading.Thread(storePic(str(c)+".jpg",i)).start()
		c+=1
	except:
		pass