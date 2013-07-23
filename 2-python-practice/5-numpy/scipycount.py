#!/usr/bin/env python
import numpy as np
import time
import random
from scipy.sparse import bsr_matrix
from scipy.sparse import rand
tStart = time.time()
x=rand(1,10000000,density=0.00001,format='bsr').todense()
y=rand(10000000,1,density=0.00001,format='bsr').todense()
for i in range(1000):
	z=x*y
print z
tEnd = time.time()
print "it cost %f sec" %(tEnd-tStart)
