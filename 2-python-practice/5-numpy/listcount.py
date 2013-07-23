#!/usr/bin/env python
import numpy as np
import time
tStart = time.time()
x = np.random.randint(10, size=(10000000))
x = list(x)
y = np.random.randint(10, size=(10000000))
x = list(y)
for i in range(10):
	t=0
	for j in range(10000000):
		t+=x[j]*y[j]
tEnd = time.time()
print "it cost %f sec" %(tEnd-tStart)
