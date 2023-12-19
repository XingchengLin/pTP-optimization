######################################################################################
# This script will help find the TS, U and F ensemble based on the peakList output from
# findHistMin.py;
# It will output a timeseries list for 0:U, 1:TS and 2:F ensemble;
#
# Written by Xingcheng Lin, 01/17/3017;
#######################################################################################

import time;
import subprocess;
import os;

################################################
def my_lt_range(start, end, step):
    while start < end:
        yield start
        start += step

def my_le_range(start, end, step):
    while start <= end:
        yield start
        start += step
#############################################

def findTS( paramList ):


    # Get current working directory
    pwd = os.getcwd();

    infile = open("Q.out", "r");
    outfile = open("TPtime.xvg", "w");

    # Read in lines from the file;

    lines = [line.strip() for line in infile];

    infile.close();

    length = len(lines);

    # Do a loop to check if each time stamp is in TP;

    # Define the unfolded/folded threshold;
    unfoldBar = float(paramList[0][0]);
    foldBar = float(paramList[0][1]);
#    firstHistMax = float(paramList[0][0]);
#    secondHistMax = float(paramList[0][1]);
#    histMin = float(paramList[1][0]);

    # The unfolded bar was defined as the average of first maximum of histogram and minimum; the folded was defined as teh average of the minimum
    # and the second maximum of histogram;

#    unfoldBar = 1.0/2.0 * (firstHistMax + histMin);
#    foldBar = 1.0/2.0 * (histMin + secondHistMax);

    # If Q value is smaller than unfoldBar, it is U ensemble; larger than foldBar, F ensemble;
    # in between, TS ensemble;
    for i in my_lt_range(0, length, 1):

        # Print to show our progress;
    #    print i;
       
        line = lines[i].split();

        if (float(line[1])<=unfoldBar):
            outfile.write(line[0] + " " + str(0) + "\n");
        elif (float(line[1])>foldBar):
            outfile.write(line[0] + " " + str(2) + "\n");
        else:
            outfile.write(line[0] + " " + str(1) + "\n");

    outfile.close();

    #############################################################
#    print "When the voice of the Silent touches my words"
#    print "I know him and therefore know myself."

    return;
