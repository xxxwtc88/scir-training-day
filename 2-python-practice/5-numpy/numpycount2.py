#!/usr/bin/env python
import numpy as np
import time
import random
tStart = time.time()
#num=np.zeros((14),dtype=np.int)+3
#num=tuple(num)
x = np.zeros((10000000),dtype=np.int)
y = np.zeros((10000000),dtype=np.int)
for i in range(100):
	ran=random.randint(0,10000000)
	x[ran]=i
	ran2=random.randint(0,10000000)
	y[ran2]=i+4 
for i in range(1000):
	z=x*y
tEnd = time.time()
print "it cost %f sec" %(tEnd-tStart)
