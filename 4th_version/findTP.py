######################################################################################
# This script will help find the transition path (TP) from a Q v.s. time data;
# It will output a file showing 0/1 (whether in TP) v.s. time data; 
#
# Written by Xingcheng Lin, 06/15/3016;
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
def clear_lists(tmp_timeList, tmp_QList):
    """Clears the temporary time and Q value lists."""
    del tmp_timeList[:]
    del tmp_QList[:]

def add_to_lists(line, tmp_timeList, tmp_QList):
    """Adds elements from the given line to the temporary time and Q value lists."""
    tmp_timeList.append(line[0])
    tmp_QList.append(line[1])
##############################################

def findTP( paramList ):

    infile = open("Q_normalized.out", "r");
    outfile = open("TPtime.xvg", "w");

    # Read in lines from the file;

    lines = [line.strip() for line in infile];

    infile.close();

    length = len(lines);

    # Do a loop to check if each time stamp is in TP;

    print("paramlist", paramList);

    # Define the unfolded/folded threshold;
    unfoldBar = float(paramList[0]);
    foldBar = float(paramList[1]);

    # Flag guiding the finding of TP, 1 for unfolded, 2 for transition, 3 for folded;
    TPflag1 = 0;
    # Another flag will mark the direction: Going from unfolded to folded or vice versus. Based on that
    # we will decide whether to dump the stored array into a TPfile;
    # 1 for unfolded->folded; 2 for vice versus; 0 for not in the transition state;
    TPflag2 = 0;
    # temporary list storing times and Q values;
    tmp_timeList = [];
    tmp_QList = [];

    # The first line output from Plumed Driver is not useful;
    for i in my_lt_range(1, length, 1):


        line = lines[i].split();

        # Here I set it as starting from the unfolded basin;

        # Get rid of the frames started above the bars and in the middle;
        if(float(line[1])>=unfoldBar and TPflag1==0):
            TPflag1 = 0;
            TPflag2 = 0;
        elif(float(line[1]) < unfoldBar and TPflag1!=2):
            TPflag1 = 1;
            TPflag2 = 0;
        elif(float(line[1]) < unfoldBar and TPflag1==2):
            TPflag1 = 1;
        elif (float(line[1]) >= unfoldBar and float(line[1]) < foldBar and TPflag1 == 1):
            TPflag1 = 2;
            TPflag2 = 1;
        elif (float(line[1]) >= unfoldBar and float(line[1]) < foldBar and TPflag1 == 2):
            TPflag1 = 2;
        elif (float(line[1]) >= unfoldBar and float(line[1]) < foldBar and TPflag1 == 3):
            TPflag1 = 2;
            TPflag2 = 2;
        elif (float(line[1]) >= foldBar and TPflag1 == 2):
            TPflag1 = 3;
        elif (float(line[1]) >= foldBar and TPflag1 == 3):
            TPflag1 = 3;
            TPflag2 = 0;
        else:
            print("Yell");
            print(line[0], line[1], TPflag1, TPflag2);
#            time.sleep(1);

        # If TPflag1 == 2 and TPflag2 == 1, start storing data into a list;
        if TPflag1 == 2 and TPflag2 == 1:
            add_to_lists(line, tmp_timeList, tmp_QList)
        elif TPflag1 == 3 and TPflag2 == 1:
            for j in my_lt_range(0, len(tmp_timeList), 1):
                outfile.write(tmp_timeList[j] + " " + str(1) + "\n")
            clear_lists(tmp_timeList, tmp_QList)
            outfile.write(line[0] + " " + str(0) + "\n")
        elif TPflag1 == 2 and TPflag2 == 2:
            add_to_lists(line, tmp_timeList, tmp_QList)
        elif TPflag1 == 1 and TPflag2 == 2:
            for j in my_lt_range(0, len(tmp_timeList), 1):
                outfile.write(tmp_timeList[j] + " " + str(1) + "\n")
            clear_lists(tmp_timeList, tmp_QList)
            outfile.write(line[0] + " " + str(0) + "\n")
        elif TPflag1 == 1 and TPflag2 == 1:
            for j in my_lt_range(0, len(tmp_timeList), 1):
                outfile.write(tmp_timeList[j] + " " + str(0) + "\n")
            clear_lists(tmp_timeList, tmp_QList)
            outfile.write(line[0] + " " + str(0) + "\n")
        elif TPflag1 == 3 and TPflag2 == 2:
            for j in my_lt_range(0, len(tmp_timeList), 1):
                outfile.write(tmp_timeList[j] + " " + str(0) + "\n")
            clear_lists(tmp_timeList, tmp_QList)
            outfile.write(line[0] + " " + str(0) + "\n")
        else:
            outfile.write(line[0] + " " + str(0) + "\n")


    outfile.close();

    #############################################################
#    print "When the voice of the Silent touches my words"
#    print "I know him and therefore know myself."

    return;