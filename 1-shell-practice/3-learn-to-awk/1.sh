#!/bin/sh
awk '{if ($(NR%2) == 0) print $1 }' 1.dat
