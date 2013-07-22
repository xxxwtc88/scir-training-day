#!/usr/bin/env python
import cPickle as pickle
import sys

def max_match_segment( line, dic ):
    # write your code here
	result=""
	maxnum,nodenum=7,3
	while True:
		if len(line)<maxnum*nodenum:
			maxnum=len(line)/nodenum
		if len(line)==0: break
		for x in range(maxnum*nodenum,0,-nodenum):
			words=line[0:x]
			if x==nodenum:
				line.replace(words,'',1)
				result+=words+"/t"
				break
			if dic.find(words):
				line.replace(words,'',1)
				result+=words+"/t"
				break
if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        dic = pickle.load(sys.argv[2])
    except:
        print >> sys.stderr, "failed to load dict"
        sys.exit(1)

    for line in fpi:
        print "\t".join( max_match_segment(line.strip(), dic) )

