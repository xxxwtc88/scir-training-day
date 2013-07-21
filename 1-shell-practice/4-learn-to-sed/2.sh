#!/bin/sh
grep -o "'.*" 2.dat  | sed "s/^'//g" | sed "s/'$//g" >2.out
