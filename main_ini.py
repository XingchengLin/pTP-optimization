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

# Get the qimap through g_kuh;
#os.environ["la"] = "/home/xl23/bin/mpigmx504sbm-v8.1-plu/bin";

#subprocess.call("$la/gmx kuh -abscut -noshortcut -cut 0.1 -f ../v504_short.xtc -n natcont.ndx -o Q.gkuh.out -s ../smog.gro -times -i qimap.out -qiformat list", shell=True);

# Read in qimap into a matrix;
infile = open("../qimap.out", "r");
matrix = [map(int,line.split()) for line in infile];
matrix = np.asarray(matrix);
# Reshape into a 1-D array;
#nRow = np.size(matrix,0);
nCol = np.size(matrix, 1);
# Number of contacts is equal to the number of columns in qimap.out file;
NoCon = nCol;
#args = matrix.flatten();
tArgs = tuple(matrix);

infile.close();

# Parallelization;
#import multiprocessing.sharedctypes;
#shared_array_base = multiprocessing.sharedctypes.Array(ctypes.c_int, args);
#shared_array = np.ctypeslib.as_array(shared_array_base.get_obj())
#shared_array = np.frombuffer(args, dtype=int);

#pool = multiprocessing.Pool(processes=3);
# Apply CG;
from nm_ini_multi import nm_ini_multi;
p1 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p1.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p1.start();
os.chdir("../");


p2 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p2.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p2.start();
os.chdir("../");

p3 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p3.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p3.start();
os.chdir("../");

p4 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p4.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p4.start();
os.chdir("../");

p5 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p5.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p5.start();
os.chdir("../");

p6 = multiprocessing.Process(target=nm_ini_multi, args=(tArgs, NoCon));
# Get the last character of the process name, which will be a number from 1 to the # of processes;
directory = "cg." + p6.name[-1];
if os.path.exists(directory):
    shutil.rmtree(directory);
bkdirectory = directory + "/backup";
os.makedirs(bkdirectory);
subprocess.call("cp *.py '%s'" %(directory), shell=True);
os.chdir(directory);
p6.start();
os.chdir("../");

