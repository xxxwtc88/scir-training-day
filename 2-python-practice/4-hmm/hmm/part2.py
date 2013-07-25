#!/usr/bin/env python
import sys
import string
import math
class computes_emission(object):
    diction={}
    TagType={"counttag_O":0,"counttag_I-GENE":0}
    fpi=open("gene.counts","r") 
    def __init__(self):
	fpi.seek(0)
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
	self.fpi.seek(0)
	for key in self.diction.keys():
            for key2 in self.diction[key].keys():
                if self.diction[key][key2]==0 :
	  	    self.diction[key][key2]=self.diction["_RARE_"][key2]
class computes_trigram:
    CountBigram={}
    CountTrigram={}
    TrigramPro={}
    fpi=open("gene.counts","r") 
    def __init__(self):
	fpi.seek(0)
        for sentence in self.read_instance(self.fpi):
	    WordsList= sentence.split()
	    if WordsList[1]=="2-GRAM" :
               temp=(WordsList[2],WordsList[3])
	       self.CountBigram[temp]=string.atol(WordsList[0])
	    elif WordsList[1]=="3-GRAM":
	       temp=(WordsList[2],WordsList[3],WordsList[4])
	       self.CountTrigram[temp]=string.atol(WordsList[0])
    def read_instance(self,fp):
        while True:
            line = fp.readline()
            if not line:
                break
            else:
	        yield line
    def computespos(self):
	self.fpi.seek(0)
	for key in self.CountTrigram.keys():
	    BiList=(key[0],key[1])
            self.TrigramPro[key]=float(self.CountTrigram[key])/self.CountBigram[BiList]
    def showout(self):
	print self.TrigramPro 
class Trigram:
	states=[]
	emissionPro={}
	TrigramPro={}
	result=[]
	def __init__(self,dic1,dic2):
		self.emissionPro=dic1
		self.TrigramPro=dic2
	def read_instance(self,fp):
    		sentence = []
    		word=''
    		while True:
        	    line = fp.readline()
        	    if not line:
  	    		sentence=word.split()
           		yield sentence
            		break
       		    line = line.strip()
       		    if len(line) == 0:
  	   		sentence= word.split()
           		yield sentence
            		sentence = []
            		word=''
        	    else:
           		word+=line+" "
	def maketag(self,fp):
	    for sentence in self.read_instance(fpi):
		if len(sentence)==0:continue
           	self.trigramap(sentence,0)
		self.countResult()
		for n in range(len(sentence)):
			print sentence[n],self.result[n]
		print ""
		self.states=[]
			
	def computeemi(self,words,tag):
		if words in self.emissionPro :
			return self.emissionPro[words][tag]
		else:
			return self.emissionPro['_RARE_'][tag]
	def countResult(self):
		bestpath=self.states[len(self.states)-1][("O","O")][1]
		self.result=[bestpath[1]]
		for n in range(len(self.states)-2,0,-1):
			bestpath=self.states[n][bestpath][1]
			self.result.insert(0,bestpath[1])
		self.result.insert(0,bestpath[0])
	def trigramap(self,sentence,n):
	    tempdic={("O","O"):[],("O","I-GENE"):[],("I-GENE","O"):[],("I-GENE","I-GENE"):[]}
	    self.states.append(tempdic)
	    if n==0:
			for key in self.states[0].keys():
				pro=math.log(self.computeemi(sentence[0],key[0])*self.computeemi(sentence[1],key[1])*self.TrigramPro[('*','*',key[0])]*self.TrigramPro[('*',key[0],key[1])])
				self.states[0][key].append(pro)
			self.trigramap(sentence,1)
			return 
	    if n<len(sentence)-1:
			for key in self.states[n].keys():
				maxpro=-100000000
				prostate=()
				for key2 in self.states[n-1].keys():
					if key[0]==key2[1]:
						pro=math.log(self.computeemi(sentence[n+1],key[1])*self.TrigramPro[(key2[0],key2[1],key[1])])+self.states[n-1][key2][0]
						if pro>maxpro:
							maxpro=pro
							prostate=key2
				self.states[n][key].append(maxpro)
				self.states[n][key].append(prostate)
			self.trigramap(sentence,n+1)
			return 
	    if n==len(sentence)-1:
	 		for key in self.states[n].keys():
				prostate=()
				maxpro=-100000000
				for key2 in self.states[n-1].keys():
					pro=math.log(self.TrigramPro[(key2[0],key2[1],'STOP')])+self.states[n-1][key2][0]
					if pro>maxpro:     
						maxpro=pro
						prostate=key2
				self.states[n][key].append(maxpro)
				self.states[n][key].append(prostate)
			return 
if __name__=="__main__":
    try:
        fpi = file(sys.argv[1],"r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read inputfile %s.\n" % arg)
        sys.exit(1)
    diction1=computes_emission()
    diction1.computespos()
    diction1.compute2()
    diction2=computes_trigram()
    diction2.computespos()
    myTrigram=Trigram(diction1.diction,diction2.TrigramPro)
    myTrigram.maketag(fpi)
