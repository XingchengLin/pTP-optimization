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
import multiprocessing;
import ctypes;
import shutil;

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

def nm_again_multi( tArgs, NoCon ):
#    shared_array = np.frombuffer(shared_array_base.get_obj(), dtype="int32");
#    tArgs = tuple(shared_array);

    # Read in the weight vector from weight_read.txt

    weight_vector = np.loadtxt('tmp_weight.txt');

    # exclude the first and the last entry;
    weight_vector_DR = weight_vector[1:-1];

#    weight_vector = [];
#    weightFile = open('tmp_weight.txt', 'r');
#    lines = [line.strip() for line in weightFile];
#    weightFile.close();
#    for i in my_lt_range(0, len(lines)-2, 1):
#        line = lines[i].split();
#        weight_vector.append(float(line[0]));
#    
#    weight_vector = np.asarray(weight_vector);
#

    # Read in the simplex from tmp_simplex.txt
    sim = np.loadtxt('tmp_simplex.txt');

    # Get the peak value of the pTPr;
    from function_multi import function_multi;
    from recordCG import recordCG;

    # Do Downhill Simplex;
    from scipy import optimize;
    res = optimize.minimize(function_multi, weight_vector_DR, args=tArgs, method='Nelder-Mead', callback=recordCG, options={'initial_simplex':sim});
    print 'res = ', res;

