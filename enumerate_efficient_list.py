import numpy as np 
import sys

string = sys.argv[1]

data = np.loadtxt(str(sys.argv[1]))
beginning_of_sequence = data[0]
for i in range(len(data)-1):
    if data [i+1] != data [i] + 1:
        print (str (int(beginning_of_sequence)) + ' ' + str(int(data[i])))
        beginning_of_sequence = data[i+1]
        
print (str (int(beginning_of_sequence)) + ' ' + str(int(data[i+1])))
