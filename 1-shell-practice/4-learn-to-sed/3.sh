#!/bin/sh
for file in `ls *.raw`
do
mv $file `echo $file | sed "s/\.raw$//"`
done
