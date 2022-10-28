import numpy as np 
import re
import sys

file = open ('alignment.ali','r+')
out_file = open ('alignment_cleaned.ali','w+')
for line in file.readlines():
    if ':' in line:
        fields = line.split(':')
        fields[2:6] = '.'*len(fields[2:6])
        line = ":".join(fields) 
    out_file.writelines(line)

