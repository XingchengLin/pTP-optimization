####################################################################################
# This script will help calculate and output pTPr based on weight.txt file; 
#
# Written by Xingcheng Lin, 12/13/2016
####################################################################################

import math;
import subprocess;
import os;
import math;
import numpy as np;
import sys;
import shutil;
import random;

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

def calpTPr_main( NoFolder ):
    # Read in qimap into a matrix;
    infile = open("qimap.out", "r");
    matrix = [map(int,line.split()) for line in infile];
    infile.close();

    # Current working directory;
    cwd = os.getcwd();
    print cwd;

    for i in my_le_range(1, NoFolder, 1):
        pathName = cwd + "/cg." + str(i);
        os.chdir(pathName);

        # Create a folder for storing the weight.txt files;
        if os.path.exists("./weightFile"):
            shutil.rmtree("./weightFile");
            os.mkdir("./weightFile");
        else:
            os.mkdir("./weightFile");

        # Count number of weight files in the folder backup/;
        NoWeightFile = int(subprocess.check_output("find backup/ -maxdepth 1 -type f | wc -l", shell=True));

	# We won't check every weight file, it is too much time;
        for j in my_lt_range(1, NoWeightFile, 20):

            # Copy the corresponding weight.txt into the current folder;
            src = "backup/weight." + str(j) + ".txt";
            dst = "./weight_read.txt";
            shutil.copy(src, dst);

            # Read in the weight vector from weight_read.txt
            weight_vector = [];
            weightFile = open('weight_read.txt', 'r');
            lines = [line.strip() for line in weightFile];
            weightFile.close();
            for i in my_lt_range(0, len(lines)-2, 1):
                line = lines[i].split();
                weight_vector.append(float(line[0]));

            weight_vector = np.asarray(weight_vector);
            # Get the peak value of the pTPr;
            from calpTPr import calpTPr
            peakPTPr = calpTPr( weight_vector, matrix );

            print peakPTPr;

            # output into a new folder;
            outfile_weight = open("tmp_weight_read.txt", "w");

            for i in my_lt_range(0, len(weight_vector), 1):
                outfile_weight.write(str(weight_vector[i]) + "\n");

            outfile_weight.write("The best pTPr is:" + "\n" + str(peakPTPr) + "\n");
            outfile_weight.close();

            # Check and copy the existence of a file, and make copy;
            for k in my_lt_range(1, 1000000, 1):
                targetFile = "weightFile/weight." + str(k) + ".txt";
                if (os.path.isfile(targetFile)):
                    pass;
                else:
                    src = "tmp_weight_read.txt";
                    shutil.copy(src, targetFile);
                    break;

    return;

############################################################################

if __name__ == "__main__":
    NoFolder = int(sys.argv[1]);
    
    calpTPr_main( NoFolder );
    
    print "I slept and dreamt that life was joy."
    print "I awoke and saw that life was service."
    print "I acted and behold, service was joy."

