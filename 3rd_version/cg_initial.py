####################################################################################
# This script will help start a Conjugate Gradient Program to optimize the weighting 
# function for calculating Q value;
# If it is in the first time usage, create a weight_read.txt file where each line is
# 1.0/NoCon and the last pTPrmax value is 0.0; 
#
# Written by Xingcheng Lin, 12/13/2016
####################################################################################

import math;
import subprocess;
import os;
import math;
import numpy as np;
import random;
import time;

################################################
def my_lt_range(start, end, step):
    while start < end:
        yield start
        start += step

def my_le_range(start, end, step):
    while start <= end:
        yield start
        start += step
###########################################

# Get the qimap through g_kuh;
#os.environ["la"] = "/home/xl23/bin/mpigmx504sbm-v8.1-plu/bin";

#subprocess.call("$la/gmx kuh -abscut -noshortcut -cut 0.1 -f ../v504_short.xtc -n natcont.ndx -o Q.gkuh.out -s ../smog.gro -times -i qimap.out -qiformat list", shell=True);

# Read in qimap into a matrix;
infile = open("../qimap.out", "r");
matrix = [map(int,line.split()) for line in infile];
matrix = np.asarray(matrix);
# Reshape into a 1-D array;
nRow = np.size(matrix,0);
nCol = np.size(matrix, 1);
# Number of contacts is equal to the number of columns in qimap.out file;
NoCon = nCol;
args = np.reshape(matrix, (1, nRow*nCol));
tArgs = tuple(args);

infile.close();

# Read in the weight vector from weight_read.txt
#weight_vector = [];
#weightFile = open('weight_read.txt', 'r');
#lines = [line.strip() for line in weightFile];
#weightFile.close();
#for i in my_lt_range(0, len(lines)-2, 1):
#    line = lines[i].split();
#    weight_vector.append(float(line[0]));
#
#weight_vector = np.asarray(weight_vector);

# Randomly generate a initial weight_vector;
weight_vector = np.random.random_sample(size=NoCon);

# Output into a tmp_weight.txt file;

outfile_weight = open("tmp_weight.txt", "w");

for i in my_lt_range(0, len(weight_vector), 1):
    outfile_weight.write(str(weight_vector[i]) + "\n");

outfile_weight.write("The best pTPr is:" + "\n" + str(0.0) + "\n");
outfile_weight.close();


# Get the peak value of the pTPr;
from function import function;
# function( weight_vector, args );

# Do Conjugate Gradient;
from scipy import optimize;
# Reshape matrix;
res = optimize.fmin_cg(function, weight_vector, fprime=None, args=tArgs, epsilon=1.0);
print 'res = ', res;

