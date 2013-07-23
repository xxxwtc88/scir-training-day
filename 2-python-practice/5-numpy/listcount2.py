#!/usr/bin/env python
import numpy as np
import time
import random
tStart = time.time()
x = np.zeros((10000000),dtype=np.int)
x = list(x)
y = np.zeros((10000000),dtype=np.int)
y = list(y)
for i in range(100):
	ran=random.randint(0,10000000)
	x[ran]=i
	ran2=random.randint(0,10000000)
	y[ran2]=i+4 	
for i in range(10):
	t=0
	for j in range(10000000):
		t+=x[j]*y[j]
tEnd = time.time()
print "it cost %f sec" %(tEnd-tStart)
