#!/bin/sh
count=0
awk '{gsub(/_[a-zA-Z]*./, ""); print }' 3.dat>3.out
