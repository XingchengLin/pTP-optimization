import sys;
import subprocess;
import os;
import shutil;
import math;
import numpy as np;
import time;
import scipy.io


####################################################################################
# This script will help calculate <qij> as a function of Q_opt
# input: weight vector; qimap.out
#
# Written by Xingcheng Lin, 08/06/2018
####################################################################################

################################################


def my_lt_range(start, end, step):
    while start < end:
        yield start
        start += step


def my_le_range(start, end, step):
    while start <= end:
        yield start
        start += step


def find_closest(A, target):
    #A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx
###########################################

def calc_Diff_qij(weightFile, qimapFile):

    weight_vector = np.loadtxt(weightFile)
    # exclude the first and the last entry;
    weight_vector_DR = weight_vector[1:-1]

    weight_vector = np.insert(weight_vector_DR, 0, 0.5)

    mdict = scipy.io.loadmat(qimapFile)
    matrix = mdict['matrix']
    del mdict

    # Multiply the matrix with its corresponding weight, add up to be the weighted Q;
    weighted_Q = np.dot(matrix, weight_vector)

    # Find the maximum and minimum value of weighted_Q values; They will be the boundaries of Q values;
    weightedQ_max = np.amax(weighted_Q)
    weightedQ_min = np.amin(weighted_Q)

    # Do feature scaling to weighted Q to be in between 0 and 1;
    weighted_Q_norm = (weighted_Q - weightedQ_min) / \
        (weightedQ_max - weightedQ_min)

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
    peakList = findHistExt()[0];

    # Calculate the peak of the hist.txt, it will demarcate the transition state;
    print("The left and right boundaries of this TS is:")
    print(peakList)
    
    # get the qij_mean_Q;
    qij_mean_Q = np.loadtxt("qij_mean_Q.txt");
    # The first column is the bin edges of Q;
    Q_binedges = qij_mean_Q[:, 0];

    # Calculate the indices of the left and right boundaries of the TS states
    TSleftIdx = find_closest(Q_binedges, peakList[0])
    TSrightIdx = find_closest(Q_binedges, peakList[1])

    print("The indices of left and right boundaries of this TS is:")
    print([TSleftIdx, TSrightIdx])

    # find the values of <qij> at this two boundaries, ignore the first column, which is the binedge of Q-optimized
    bValues_qij = qij_mean_Q[[TSleftIdx, TSrightIdx], 1:]

    # calculate the delta<qij> (of TS boundaries)
    diff_qij = bValues_qij[1, :] - bValues_qij[0, :]

    np.savetxt('delta_qij_TS.txt', diff_qij, fmt='%.3f')

    


############################################################################


if __name__ == "__main__":
    weightFile = sys.argv[1]
    qimapFile = sys.argv[2]

    calc_Diff_qij(weightFile, qimapFile)
    print("When the voice of the Silent touches my words,")
    print("I know him and therefore know myself.")
