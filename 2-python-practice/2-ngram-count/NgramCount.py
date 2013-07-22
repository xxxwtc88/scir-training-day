#!/usr/bin/env python
import ngramcount
import sys
def read_instance(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        else:
	    yield line
if __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)
    onegram=ngramcount.NGram(1)
    bigram=ngramcount.NGram(2)
    for sentence in read_instance(fpi):
        onegram.scan(sentence)
	bigram.scan(sentence)
    sys.stdout = open("data.uni", "write") 
    for key in onegram.diction1.keys():
	print "%s %s" %(key,onegram.diction1[key]) 
    sys.stdout = open("data.bi", "write") 
    for key in bigram.diction2.keys():
	print "%s %s %s" %(key[0],key[1],bigram.diction2[key] )
