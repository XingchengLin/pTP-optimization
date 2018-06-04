###########################################################################
# This script will help find the extrema of histQ.txt;
# 
# Written by Xingcheng Lin, 12/12/2016;
###########################################################################

###########################################################################
# This script will help calculate the PMF
# 
# Written by Xingcheng Lin, 12/12/2016;
###########################################################################

import time;
import subprocess;
import os;
import math;
import numpy as np;


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

def findHistExt():
    infile = open("histQ_smooth.txt", "r");

    # Read in lines from the file;
    lines = [line.strip() for line in infile];

    infile.close();

    length = len(lines);

    # For the two peaks histograms, we will find the cusps according to the trend where values go up and down;
    value = 0.0;
    xtmp = 0.0;
    flag = 0;
    maxList = [];
    maxValueList = [];
    minList = [];
    minValueList = [];

    for i in my_lt_range(0, length, 1):

        line = lines[i].split();
        if ((flag == 0 or flag == 1) and float(line[1]) > value):
            # flag = 1 means it is in the first ascending trend;
            flag = 1;
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif (flag == 1 and float(line[1]) < value and float(line[1]) > 0.01):
            # flag = 2.1 means it is in the descending trend for the first time, we set a value threshold of 0.01 so that it will 
            # have to be larger than that to be identified as the descending mode from the first peak;
            flag = 2.1;
            value = float(line[1]);
        elif (flag == 2.1 and float(line[1]) < value):
            # flag = 2.2 means it is in the descending trend for the second time;
            flag = 2.2;
            value = float(line[1]);
        elif (flag == 2.2 and float(line[1]) < value):
            # flag = 2.3 means it is in the descending trend for the 3rd time;
            flag = 2.3;
            # Record the value of the first maximum;
            maxList.append(xtmp);
            maxValueList.append(xValuetmp);
            value = float(line[1]);
            xtmp = float(line[0]);            
            xValuetmp = float(line[1]);
        elif (flag == 2.3 and float(line[1]) < value):
            # flag = 2.3 means it is still in the descending trend;
            flag = 2.3;
            value = float(line[1]);
            xtmp = float(line[0]);            
            xValuetmp = float(line[1]);
        elif ((flag == 2.1 or flag == 2.2) and float(line[1]) > value):
            # flag = 1 means the first descending is fluctuation;
            flag = 1;
            value = float(line[1]);
            xtmp = float(line[0]);  
            xValuetmp = float(line[1]);
        elif (flag == 2.3 and float(line[1]) > value):
            # flag = 3.1 means it is again in the ascending trend for the first time;
            flag = 3.1;
            value = float(line[1]);
        elif (flag == 3.1 and float(line[1]) > value):
            # flag = 3.2 means it is again in the ascending trend for the second time;
            flag = 3.2;
            value = float(line[1]);
        elif (flag == 3.2 and float(line[1]) > value):
            # flag = 3.3 means it is again in the ascending trend for the second time;
            flag = 3.3;
            # Record the value of the minimum;
            minList.append(xtmp);
            minValueList.append(xValuetmp);
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif (flag == 3.3 and float(line[1]) > value):
            # flag = 3.3 means it is again in the ascending trend for the 3rd time;
            flag = 3.3;
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif ((flag == 3.1 or flag == 3.2) and float(line[1]) < value):
            # flag = 2.3 means the former descending is fluctuation;
            flag = 2.3;
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif (flag == 3.3 and float(line[1]) < value and float(line[1]) > 0.01 and (float(line[0])-maxList[0]) > 0.1):
            # flag = 4.1 means it is again in the descending trend for the first time, we set a value threshold of 0.01 so that it will 
            # have to be larger than that to be identified as the descending mode from the second peak; And we set it up that this descending
            # mode has to be at least 0.1 away from the first cusp;
            flag = 4.1;
            value = float(line[1]);
        elif (flag == 4.1 and float(line[1]) < value):
            # flag = 4.2 means it is again in the descending trend for the second time;
            flag = 4.2;
            value = float(line[1]);
        elif (flag == 4.2 and float(line[1]) < value):
            # flag = 4.2 means it is again in the descending trend for the 3rd time;
            flag = 4.3;
            # Record the value of the second maximum;
            maxList.append(xtmp);
            maxValueList.append(xValuetmp);
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif (flag == 4.3 and float(line[1]) < value):
            # flag = 4.3 means it is still in the descending trend;
            flag = 4.3;
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);
        elif ((flag == 4.1 or flag == 4.2) and float(line[1]) > value):
            # flag = 3.3 means the previous descending is fluctuation;
            flag = 3.3;
            value = float(line[1]);
            xtmp = float(line[0]);
            xValuetmp = float(line[1]);

#        Print out debugging information;
#        print (line[0], flag, value);

    print [maxList, minList];

    # Based on that, let us find the boundary of Transition state, which is defined as the P that is e times of Pmin (so that their free energy differece is 1K_BT);
    infile = open("histQ_smooth.txt", "r");
    
    matrix = [map(float, line.split()) for line in infile];
    matrix = np.asarray(matrix);
    infile.close();

    nRow = np.size(matrix, 0);
    flag = 0;
    
    peakList = [];
    for i in my_lt_range(0, nRow, 1):
        
        if (matrix[i][0] == maxList[0]):
            flag = 1;

        if (flag == 1 and matrix[i][1] > 2.71828*minValueList[0] and matrix[i+1][1] < 2.71828*minValueList[0]):
            flag = 2;
            peakList.append(matrix[i][0]);

        if (flag == 2 and matrix[i][1] < 2.71828*minValueList[0] and matrix[i+1][1] > 2.71828*minValueList[0]):
            flag = 3;
            peakList.append(matrix[i][0]);


    print peakList;


    return [peakList, minList];




