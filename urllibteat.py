import urllib
import time
import os



def close_psiphon():
    try:
        os.system('TASKKILL /IM psiphon3.exe')
    except Exception, e:
        print str(e)


close_psiphon()
time.sleep(10)
stri = "http://192.168.1.5:8090/httpclient.html"
data = urllib.urlopen(stri)
print data
