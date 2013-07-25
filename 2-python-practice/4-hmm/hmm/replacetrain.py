#!/usr/bin/env python
import sys
def read_instance(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        else:
	    yield line
class CountFre(object):
    diction = {}
 

    def scan(self, sentence):
	WordsList=()
	WordsList= sentence.split() 
	self.ngram(WordsList)

    def ngram(self, words):
	if len(words)>1:
		self.diction[words[0]]=self.diction.get(words[0],0)+1

if __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)
    mydiction=CountFre()
    for sentence in read_instance(fpi):
        mydiction.scan(sentence)
    fpi.seek(0) 
    sys.stdout = open("newgene.train", "write") 
    for sentence in read_instance(fpi):
	WordsList= sentence.split() 
	if  len(WordsList)>0 and mydiction.diction.get(WordsList[0],0)<5 :
		print "_RARE_ %s" %(WordsList[1])
	else :
		print "%s" %(sentence.strip()) 
