import numpy as np 
import re
import os 

#this script will use the last column in the log file for scoring lines as the parameter to sort the models by
#to do: detect scoring function

#place to store lines which look like 
#pdbname.BL00001.pdb molpdfscore DOPESCORE 
model_lines=list([])
#read log file in reverse. assumed that run has been successful and is outputting results of scoring of each model.
#check if line contains pattern which indicates we have read in all the scoring lines of the log file
#only read in line if it is greater than 1 in length 
for line in reversed(list(open("log.log"))):
    if (re.search ('>> Summary of successfully produced',line)):
        #getting rid of dashes line and metadata line 
        model_lines=model_lines[:-2]
        break 
    if (len (line) > 1):
        model_lines.append([line])

#convert from annoying strings to useful datatypes
files = ['']*len(model_lines)
scores = np.zeros(len(model_lines))
for i in range(len(model_lines)):
        files[i] = model_lines[i][0].split()[0]
        scores[i] = np.float(model_lines[i][0].split()[-1])


#sort scores and then use those indexes to sort the files names too. Note that if we're not using DOPE we need to reverse the sorting because dope is negative
#if not DOPE
#sort_inds=sort_inds[::-1]

sort_inds = np.argsort(scores)
sorted_files = (np.array(files)[sort_inds])

f=open('ordered.txt','w+')
for i in range(len(sorted_files)):
    f.write(str(sorted_files[i]) + '\n')

