import os
import datetime
import time
import urllib2

for i in range(0,6) :
 dtlog= datetime.datetime.now()-datetime.timedelta(seconds=10)
# dtlog= datetime.datetime.now()
 dtlog= dtlog.strftime("%b %d %H:%M:%S")[:-1]
 cat='cat /var/log/syslog|grep "'+dtlog+ '"|grep "svxreflector svxreflector"|grep -E  "Login OK|Connection closed"'
# print(cat)
 ex=os.popen(cat).read().split("\n")
 for li in ex:
  if (len(li)>0):
   type="NC"
   if (li.find("Login OK")>-1):
    type="971"
   li=li.split("]:")
   li=li[1].split(":")
   li=li[0].split(")")
#   li=li.replace(" ","-")
   li=li[0].strip().split(" ")
   r=li[1].strip()
   if (len(r)>0):
    url="https://radioamateur.gp/rrf.php?s="+type+"&c="+r
    print(url)
    urllib2.urlopen(url).read()
 time.sleep(10)
