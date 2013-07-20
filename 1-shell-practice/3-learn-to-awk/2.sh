#!/bin/sh
count=0
awk '{count+=$2; print $0 " " count}' 2.dat>2.out
