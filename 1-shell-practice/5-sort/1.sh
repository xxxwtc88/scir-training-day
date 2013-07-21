#!/bin/sh
sort query_log.txt | uniq -c  | sort -k 1 -n -r | sed -n '1,100p'>1.out 
