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

## Read in qimap into a matrix;
#matrix = np.loadtxt("../qimap.out", dtype='int8');
#scipy.io.savemat('../qimap.mat', {'matrix': matrix});

mdict = scipy.io.loadmat("../qimap.mat");
matrix = mdict['matrix'];
del mdict;

# Parallelization;
from multiprocessing import sharedctypes
X_size = np.size(matrix)
X_shape = np.shape(matrix)
X_ctypes = multiprocessing.sharedctypes.RawArray('d', X_size)
X_ctypes_np = np.frombuffer(X_ctypes, dtype='float').reshape(X_shape)
# Copy data to our shared array;
np.copyto(X_ctypes_np, matrix)
tArgs = (X_ctypes, X_shape)


# Apply CG;
from nm_ini_multi import nm_ini_multi;
p1 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p1.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p1.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p2 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p2.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p2.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p3 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p3.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p3.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p4 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p4.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p4.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p5 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p5.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p5.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p6 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p6.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p6.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p7 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p7.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p7.start();
os.chdir("../");

from nm_ini_multi import nm_ini_multi;
p8 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs,));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
folderLabel = filter(str.isdigit, p8.name)
directory = "cg." + folderLabel;
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p8.start();
os.chdir("../");
