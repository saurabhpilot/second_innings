# !/usr/bin/python

def reverseword(x):
    y=""
    a=x.split(" ")
    a.reverse()
    for item in a:
    	y=y+item+" "
    return y

def reverseword1(x):
    y=""
    a=x.split(" ")
    a.reverse()
    y=" ".join(a)
    return y

if __name__=='__main__':
    x = raw_input("Enter the word to reverse: ")
    print reverseword(x)
    print reverseword1(x)
