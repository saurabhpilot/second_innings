# !/usr/bin/python

import sys
import re

def readfiles(filename):
    f=open(filename,'r')
    read_obj=f.read()

    x=re.search(r'e',read_obj)
    if x:
    	print x.group(0)
    else:
	print "fail"
    	
if __name__=='__main__':
    print 'x'
    filename='text.txt'
    readfiles(filename)
