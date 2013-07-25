#!/usr/bin/env python
import sys
import string
class computes_emission(object):
    diction={}
    TagType={"counttag_O":0,"counttag_I-GENE":0}
    fpi=open("gene.counts","r") 
    def __init__(self, f):
        self.fpi=f
        for sentence in self.read_instance(self.fpi):
	    WordsList= sentence.split()
	    if WordsList[1]=="WORDTAG" :
               self.diction[WordsList[3]]={"O":0,"I-GENE":0}
	       if WordsList[2]=="O" :
                  self.TagType["counttag_O"]+=string.atol(WordsList[0])
	       else :
	          self.TagType["counttag_I-GENE"]+=string.atol(WordsList[0])
    def read_instance(self,fp):
        while True:
            line = fp.readline()
            if not line:
                break
            else:
	        yield line
    def computespos(self):
	self.fpi.seek(0)
	for sentence in self.read_instance(self.fpi):
	    WordsList= sentence.split()
	    if WordsList[1] == "WORDTAG" :
	       if WordsList[3] != "_RARE_" :
                  pos=float(string.atol(WordsList[0]))/self.TagType["counttag_"+WordsList[2]]
                  self.diction[WordsList[3]][WordsList[2]]=pos
	       else :
	          pos=float(1)/self.TagType["counttag_"+WordsList[2]]
                  self.diction[WordsList[3]][WordsList[2]]=pos
    def compute2(self):
	for key in self.diction.keys():
            for key2 in self.diction[key].keys():
                if self.diction[key][key2]==0 :
	  	    self.diction[key][key2]=self.diction["_RARE_"][key2]

if __name__=="__main__":
    try:
        fpi = open("gene.counts", "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)
    comnow=computes_emission(fpi)
    comnow.computespos()
    try:
        fpi2 = file(sys.argv[1],"r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read inputfile %s.\n" % arg)
        sys.exit(1)
    tagO=comnow.diction["_RARE_"]["O"]
    tagI=comnow.diction["_RARE_"]["I-GENE"]
    maxtag=''
    if tagO > tagI: maxtag="O"
    else : maxtag="I-GENE"  
    for words in comnow.read_instance(fpi2):
        words=words.strip()
	if len(words) > 0:
             if words in comnow.diction :
                    if comnow.diction[words]["O"] >comnow.diction[words]["I-GENE"]: print "%s O" %words
                    else : print "%s I-GENE"  %words  
             else:
		    print "%s %s"  %(words,maxtag)
        else:
             print "" 
