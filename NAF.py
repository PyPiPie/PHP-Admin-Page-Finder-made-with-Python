import urllib2
from urllib2 import *
import requests

find=raw_input("Enter url: ")
f=open("Urls.txt","r")
sub=f.readline()
pls="http://"
req_link=pls+find+str(sub)
test=urllib2.urlopen(req_link).getcode()
if test==200:
    print 'Admin page',req_link
else:
    print 'Failure acquiring target'
