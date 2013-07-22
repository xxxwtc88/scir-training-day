#!/usr/bin/env python

class NGram(object):
    diction1 = {}
    diction2 = {}
    n=0
    def __init__(self, n):
        # n is the order of n-gram language model
        self.n = n

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
	WordsList=()
	WordsList= sentence.split() 
	self.ngram(WordsList)
        # file your code here

    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   int         count of the ngram
    def ngram(self, words):
	if self.n == 1:
		for x in range(len(words)):
			self.diction1[words[x]]=self.diction1.get(words[x],0)+1
	elif self.n  == 2:
		for x in range(len(words)-1):
			bigramnode=(words[x],words[x+1])
			self.diction2[bigramnode]=self.diction2.get(bigramnode,0)+1
        # file your code here


if __name__=="__main__":
    import sys
    print >> sys.stderr, "library is not runnable"
