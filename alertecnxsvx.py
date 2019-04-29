import os
import datetime
import time
import urllib2
import re

for i in range(0,6) :
 dtlog= datetime.datetime.now()-datetime.timedelta(seconds=10)
 dtlog= dtlog.strftime("%b %d %H:%M:%S")[:-1]
# dtlog= dtlog.strftime("%b ")[:-1]
 cat='cat /var/log/syslog|grep "'+dtlog+ '"|grep "svxreflector svxreflector"|grep -E  "Login OK|Connection closed|Heartbeat timeout"'
 print(cat)
 ex=os.popen(cat).read().split("\n")
 for li in ex:
  if (len(li)>0):
   print(li)
   type="0"
   r=""
   if (li.find("Login OK")>-1):
    type="1"
   li2=li.split("]:")
   li2=li2[1].split(":")
   li2=li2[0].strip().split(":")
   li2=li2[0].split(")")
   if (len(li2)>0):
    li2=li2[1].strip().replace(" ","-")
#    li2=li2.split("-")
#    li2=li2[0].strip()
    r=li2.strip()
   ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', li )
   if (len(ip)>0):
    ip = ip[0]
   else:
    ip=""
   if (len(r)>0):
    url="https://radioamateur.gp/antilles.php?s="+type+"&c="+r+"&i="+ip
    print(url)
    urllib2.urlopen(url).read()
 time.sleep(10)
