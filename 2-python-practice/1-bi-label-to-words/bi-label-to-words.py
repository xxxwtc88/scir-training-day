#!/usr/bin/env python
import sys

def read_instance(fp):
    sentence = []
    word=''
    while True:
        line = fp.readline()
        if not line:
  	    sentence.append( word.split() )
            yield sentence
            break

        line = line.strip()

        if len(line) == 0:
  	    sentence.append( word.split() )
            yield sentence
            sentence = []
            word=''
        else:
            node=[]
            node=line.split()
	    word += bi2words(node)	


def bi2words(chars):
    if chars[1] == 'B':
    	return ' '+chars[0]
    else:
    	return chars[0] 
    # insert your code here


if __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    try:
        fpo = open(sys.argv[2], "w")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    for sentence in read_instance(fpi):
        print sentence
