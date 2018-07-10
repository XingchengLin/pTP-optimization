####################################################################################
# This script will help calculate Phi value based on Peter and Sam Cho's 2005 PNAS
# paper;
#
# Written by Xingcheng Lin, 01/17/2016
####################################################################################

import math;
import subprocess;
import os;
import math;
import numpy as np;
import sys;

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

def phiValue():

    # Read in qimap into a matrix;
    infile = open("qimap.out", "r");
    matrix = [map(int,line.split()) for line in infile];
    matrix = np.asarray(matrix);
    infile.close();

    # Read in the weight vector from weight_read.txt
    weight_vector = [];
    weightFile = open('weight_read.txt', 'r');
    lines = [line.strip() for line in weightFile];
    weightFile.close();
    for i in my_lt_range(0, len(lines)-2, 1):
        line = lines[i].split();
        weight_vector.append(float(line[0]));

    weight_vector = np.asarray(weight_vector);
    NoCon = len(weight_vector);

    # Multiply the matrix with its corresponding weight, add up to be the weighted Q;
    weighted_Q = np.dot(matrix, weight_vector);
    
    print weight_vector;
    print weighted_Q;
    # Find the maximum and minimum value of weighted_Q values; They will be the boundaries of Q values;
    weightedQ_max = np.amax(weighted_Q);
    weightedQ_min = np.amin(weighted_Q);

    # Do feature scaling to weighted Q to be in between 0 and 1;
    weighted_Q_norm = (weighted_Q - weightedQ_min) / (weightedQ_max - weightedQ_min);

    outfile = open("Q.out", "w");

    for i in my_lt_range(0, len(weighted_Q_norm), 1):
        outfile.write(str(i) + "\t" + str(weighted_Q_norm[i]) + "\n");

    outfile.close();

    # Calculate the free energy plot;
    topRC = 1.0;
    bottomRC = 0.0;
    stepRC = 0.01; # We decided to have 100 number of bins;
    inputName = "Q.out";
    output1Name = "histQ.txt";
    output2Name = "histQ_smooth.txt";
    output3Name = "FvQ.txt";

    paramList = [topRC, bottomRC, stepRC, inputName, output1Name, output2Name, output3Name];

    from fenergy import fenergy
    fenergy( paramList );

    from findHistExt import findHistExt
    peakList = findHistExt();

    print peakList;

    # Calculate for TS, U, and F ensemble;
    from findTS import findTS
    findTS( peakList );

    # Sort according to the first column so that the time will keep increasing;
    # This is because findTP.py does not output in a increasing-time manner;
    subprocess.call("sort -s -n -k 1,1 TPtime.xvg > TPtime.sort.xvg", shell=True);

    # Get QU, QTS and QF files;
#    import shlex;
#    command_line = "paste TPtime.sort.xvg qimap.out | awk '{if($2==0) $1=$2=" + "\"\"" + "; print $0}'>qimapU.out";
#    args = shlex.split(command_line);
#    subprocess.Popen(args);
    subprocess.call("paste TPtime.sort.xvg qimap.out | awk '{if($2==0) {$1=$2=\"\"; print $0}}'>qimapU.out", shell=True);
    subprocess.call("paste TPtime.sort.xvg qimap.out | awk '{if($2==1) {$1=$2=\"\"; print $0}}'>qimapTS.out", shell=True);
    subprocess.call("paste TPtime.sort.xvg qimap.out | awk '{if($2==2) {$1=$2=\"\"; print $0}}'>qimapF.out", shell=True);
    
    # Calculate Pij for U, TS and F;
    infile = open("qimapU.out", "r");
    matrix = [map(int,line.split()) for line in infile];
    matrix = np.asarray(matrix);
    infile.close();

    nRow = np.size(matrix, 0);
    # Calculate the probability;
    ProbU = np.sum(matrix, axis=0) / float(nRow);

    # Calculate Pij for U, TS and F;
    infile = open("qimapTS.out", "r");
    matrix = [map(int,line.split()) for line in infile];
    matrix = np.asarray(matrix);
    infile.close();

    nRow = np.size(matrix, 0);
    # Calculate the probability;
    ProbTS = np.sum(matrix, axis=0) / float(nRow);

    # Calculate Pij for U, TS and F;
    infile = open("qimapF.out", "r");
    matrix = [map(int,line.split()) for line in infile];
    matrix = np.asarray(matrix);
    infile.close();

    nRow = np.size(matrix, 0);
    # Calculate the probability;
    ProbF = np.sum(matrix, axis=0) / float(nRow);

    # Calculate Phi_ij(sim) according to the Sam Cho formula;
    phi_ijSim = (ProbTS - ProbU) / (ProbF - ProbU);

    # Calculate weighted Phi_ij(sim);
    phi_ijSim_w = np.multiply(weight_vector, phi_ijSim);

    # Output;
    outfile1 = open("Phi_ij.xvg", "w");
    outfile2 = open("weightedPhi_ij.xvg", "w");

    for i in my_lt_range(0, len(phi_ijSim_w), 1):
        outfile1.write(str(phi_ijSim[i]) + "\n");
        outfile2.write(str(phi_ijSim_w[i]) + "\n");
    outfile1.close();
    outfile2.close();

    # Calculate the phi_iSim;
    NoResidue = 97;
    phi_iSim = [0.0] * NoResidue;
    count_iSim = 0;
    weightedphi_iSim = [0.0] * NoResidue;
    count_weightediSim = 0;

    infile1 = open('natcont.ndx', 'r');
    infile2 = open('Phi_ij.xvg', 'r');
    infile3 = open('weightedPhi_ij.xvg', 'r');
    outfile_phi = open('Phi_i.xvg', 'w');
    outfile_wphi = open('weightedPhi_i.xvg', 'w');
    lines1 = [line.strip() for line in infile1];
    lines2 = [line.strip() for line in infile2];
    lines3 = [line.strip() for line in infile3];
    length = len(lines1);
    
    # Make resid start from 1 instead of 0, as it should be; but note the arrays phi_iSim and weightedphi_iSim starts recording as zero based;
    for i in my_le_range(1, NoResidue, 1):
        i2 = i - 1; # note the arrays phi_iSim and weightedphi_iSim starts recording as zero based;
        count_iSim = 0;
        count_weightediSim = 0;
        # Note the first of natcont.ndx line is a trash line, so we can start form 1-based;
        for j in my_lt_range(1, length, 1):
            line1 = lines1[j].split();
            j2 = j-1; # this is because Phi_ij.xvg and weightedPhi_ij.xvg do not have the first trash line;
            line2 = lines2[j2].split();
            line3 = lines3[j2].split();

            if (int(line1[0])==i or int(line1[1])==i):
                count_iSim += 1;
                count_weightediSim += 1;
                phi_iSim[i2] += float(line2[0]);
                weightedphi_iSim[i2] += float(line3[0]);

        # Do normalization for each residue, only output the one with data;
        if (count_iSim != 0):
            phi_iSim[i2] /= count_iSim;
            weightedphi_iSim[i2] /= count_weightediSim;
            outfile_phi.write(str(i) + "\t" + str(phi_iSim[i2]) + "\n");
            outfile_wphi.write(str(i) + "\t" + str(weightedphi_iSim[i2]) + "\n");       
                
    outfile_phi.close();
    outfile_wphi.close();


    
    return;

############################################################################

if __name__ == "__main__":
    phiValue();
    print "When the voice of the Silent touches my words,"
    print "I know him and therefore know myself."

