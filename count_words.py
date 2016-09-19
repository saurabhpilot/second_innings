# !/usr/bin/python
import sys
import string

def count_words(fname):
    count = {}
    try:
    	f = open(fname)
    except:
     	print 'File cannot be opened', fname
    	sys.exit(1)
    for line in f:
    	line = line.translate(None, string.punctuation)
    	line = line.lower()
        words = line.split()
    	for word in words:
    	    	count[word] = count.get(word,0) + 1
    return count

def main():
    args = sys.argv[1:]
    print args
    if not args:
	print ' missing required args -filename'
    	sys.exit(1)
    for filename in args:
    	print count_words(filename)

if __name__=='__main__':
   main()
    	
