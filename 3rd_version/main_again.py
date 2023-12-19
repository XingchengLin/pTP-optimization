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
import scipy.io
import sys

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

# Read in qimap into a matrix;
mdict = scipy.io.loadmat("../qimap.mat");
matrix = mdict['matrix'];
del mdict;

# Number of contacts is equal to the number of columns in qimap.out file;
NoCon = np.shape(matrix)[1]

#tArgs = tuple(matrix);

## Making it a shared memory object;
#import SharedArray as sa
#sa.delete("shm://test")
#tArgs = sa.create("shm://test", np.shape(matrix), dtype='int8')
#
# Parallelization;
from multiprocessing import sharedctypes
X_size = np.size(matrix)
X_shape = np.shape(matrix)
X_ctypes = multiprocessing.sharedctypes.RawArray('d', X_size)
X_ctypes_np = np.frombuffer(X_ctypes, dtype='float').reshape(X_shape)
# Copy data to our shared array;
np.copyto(X_ctypes_np, matrix)
tArgs = (X_ctypes, X_shape)
#tArgs = np.frombuffer(tArgs_ctypes, dtype='int8', count=size)

# Apply CG;
from nm_again_multi import nm_again_multi;
p1 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p1.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p1.start();
os.chdir("../");


p2 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p2.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p2.start();
os.chdir("../");

p3 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p3.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p3.start();
os.chdir("../");

p4 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p4.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p4.start();
os.chdir("../");

p5 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p5.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p5.start();
os.chdir("../");

p6 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p6.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p6.start();
os.chdir("../");

p7 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p7.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p7.start();
os.chdir("../");

p8 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p8.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p8.start();
os.chdir("../");

p9 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p9.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p9.start();
os.chdir("../");

p10 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p10.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p10.start();
os.chdir("../");

p11 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p11.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p11.start();
os.chdir("../");

p12 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p12.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p12.start();
os.chdir("../");

p13 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p13.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p13.start();
os.chdir("../");

p14 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p14.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p14.start();
os.chdir("../");

p15 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p15.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p15.start();
os.chdir("../");

p16 = multiprocessing.Process(target=nm_again_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p16.name)
directory = "cg." + folderLabel;
os.chdir(directory);
p16.start();
os.chdir("../");
