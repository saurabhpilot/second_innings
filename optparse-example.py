# !/usr/bin/env python

from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename", version="%prog 1.0")
    parser.add_option("-u","--user",action="store",dest="username",default="admin",help="username")
    parser.add_option("-p","--pass",action="store",dest="password",default="admin",help="password")
    (options,args)=parser.parse_args()

    if len(args) !=1:
    	parser.error("Wrong number of arguments")
    print options
    print args

if __name__=='__main__':
    main()
