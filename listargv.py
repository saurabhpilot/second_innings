# !/usr/bin/python

import sys

def listargv():
    lista =[]
    if(len(sys.argv)==1):
    	print "not arguments provided"
    else:
      	sys.argv.pop(0)
    	for item in sys.argv:
    	    lista.append(item)
    	return lista

if __name__=='__main__':
    print listargv()
