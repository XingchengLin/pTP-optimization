####################################################################################
# This script will help record weight vector after each Conjugate iteraction;
#
# Written by Xingcheng Lin, 02/24/2017
####################################################################################

import math;
import subprocess;
import os;
import math;
import numpy as np;
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

def recordCG( sim, fsim ):

    # The first item of weight_vector is restricted to a constant value 0.5;
    weight_vector_DR = sim[0];
    pTPr = -fsim[0];
    weight_vector = np.insert(weight_vector_DR, 0, 0.5);
    # The last item of weight_vector is the pTPr value;
    weight_vector = np.append(weight_vector, pTPr);


    np.savetxt('tmp_weight.txt', weight_vector, fmt='%6f');
    np.savetxt('tmp_simplex.txt', sim, fmt='%6f');

    # Check and copy the existence of a file, and make copy;
    for i in my_lt_range(1, 1000000, 1):
        targetFile = "backup/weight." + str(i) + ".txt";
        if (os.path.isfile(targetFile)):
            pass;
        else:
            src = "tmp_weight.txt";
            shutil.copy(src, targetFile);
            break;

    for i in my_lt_range(1, 1000000, 1):
        targetFile = "backup/simplex." + str(i) + ".txt";
        if (os.path.isfile(targetFile)):
            pass;
        else:
            src = "tmp_simplex.txt";
            shutil.copy(src, targetFile);
            break;

    return;

############################################################################
print "Love is an endless mystery,"
print "for it has nothing else to explain it."

