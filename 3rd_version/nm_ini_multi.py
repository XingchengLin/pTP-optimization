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

def nm_ini_multi( tArgs ):

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
    

    # The Number of contacts is the column of the contact matrix;
    X_shape = tArgs[1]
    NoCon = X_shape[1]
    
    # Randomly generate a initial weight_vector;
    pid = os.getpid();
    
    # change random seed;
    np.random.seed(pid);

    # restrict one dimension to be a constant number (dimension reduction to avoid many minima in optimization);
    N_weight_vector_DR = NoCon - 1;

    weight_vector_DR = np.random.random_sample(size=N_weight_vector_DR);
    # The first iterm of weight_vector is restricted to a constant value 0.5;
    weight_vector = np.insert(weight_vector_DR, 0, 0.5);
    # The last item of weight_vector is the pTPr value, initialized as 0;
    weight_vector = np.append(weight_vector, 0);

    # Output the initial weight into a tmp_weight.txt file; weight_vector_ptpr append the ptpr value to weight_vector;

    np.savetxt('tmp_weight.txt', weight_vector, fmt='%.6f');

    #outfile_weight = open("tmp_weight.txt", "w");

    #for i in my_lt_range(0, len(weight_vector), 1):
    #    outfile_weight.write(str(weight_vector[i]) + "\n");

    #outfile_weight.write("The best pTPr is:" + "\n" + str(0.0) + "\n");
    #outfile_weight.close();

    # Check and copy the existence of a file, and make copy;
    for i in my_lt_range(1, 1000000, 1):
        targetFile = "backup/weight." + str(i) + ".txt";
        if (os.path.isfile(targetFile)):
            pass;
        else:
            src = "tmp_weight.txt";
            shutil.copy(src, targetFile);
            break;

    # Create and output the initial simplex;
    
    nonzdelt = 1.0;
    zdelt = 0.005;

    sim = np.zeros((N_weight_vector_DR + 1, N_weight_vector_DR), dtype=weight_vector_DR.dtype);

    # Initialize the simplex as random number between [0, 1);
    sim[0] = weight_vector_DR;
    for i in my_le_range(1, N_weight_vector_DR, 1):
        sim[i] = np.random.random_sample(size=N_weight_vector_DR);


#    sim[0] = weight_vector_DR;
#    for i in range(N_weight_vector_DR):
#        y = np.array(weight_vector_DR, copy=True);
#        if y[i] != 0:
#            y[i] = (1 + nonzdelt)*y[i];
#        else:
#            y[i] = zdelt;
#        sim[i + 1] = y;

    # Output to file;
    np.savetxt("tmp_simplex.txt", sim, fmt='%.6f');

    for i in my_lt_range(1, 1000000, 1):
        targetFile = "backup/simplex." + str(i) + ".txt";
        if (os.path.isfile(targetFile)):
            pass;
        else:
            src = "tmp_simplex.txt";
            shutil.copy(src, targetFile);
            break;

    # Get the peak value of the pTPr;
    from function_multi import function_multi;
    from recordCG import recordCG;

    # Do Downhill Simplex;
    from scipy import optimize;
    res = optimize.minimize(function_multi, weight_vector_DR, args=tArgs, method='Nelder-Mead', callback=recordCG, options={'initial_simplex':sim});
    print 'res = ', res;

