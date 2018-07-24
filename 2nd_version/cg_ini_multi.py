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

def cg_ini_multi( tArgs, NoCon ):
#    shared_array = np.frombuffer(shared_array_base.get_obj(), dtype="int32");
#    tArgs = tuple(shared_array);

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
    pid = os.getpid();
    # change random seed;
    np.random.seed(pid);
    weight_vector = np.random.random_sample(size=NoCon);

    # Output the initial weight into a tmp_weight.txt file;

    outfile_weight = open("tmp_weight.txt", "w");

    for i in my_lt_range(0, len(weight_vector), 1):
        outfile_weight.write(str(weight_vector[i]) + "\n");

    outfile_weight.write("The best pTPr is:" + "\n" + str(0.0) + "\n");
    outfile_weight.close();

    # Check and copy the existence of a file, and make copy;
    for i in my_lt_range(1, 1000000, 1):
        targetFile = "backup/weight." + str(i) + ".txt";
        if (os.path.isfile(targetFile)):
            pass;
        else:
            src = "tmp_weight.txt";
            shutil.copy(src, targetFile);
            break;




    # Get the peak value of the pTPr;
    from function_multi import function_multi;
    from recordCG import recordCG;

    # Do Conjugate Gradient;
    from scipy import optimize;
    # Reshape matrix;
    res = optimize.fmin_cg(function_multi, weight_vector, fprime=None, args=tArgs, epsilon=1.0, callback=recordCG);
    print 'res = ', res;

