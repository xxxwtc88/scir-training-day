#!/usr/bin/env python
import numpy as np
import time
tStart = time.time()
#num=np.zeros((14),dtype=np.int)+3
#num=tuple(num)
x = np.random.randint(10, size=(10000000))
y = np.random.randint(10, size=(10000000))
for i in range(1000):
	z=x*y
tEnd = time.time()
print "it cost %f sec" %(tEnd-tStart)
