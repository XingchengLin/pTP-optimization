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
###########################################

def calc_qij_Q(weightFile, qimapFile):

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

    No_qij = np.shape(matrix)[1]

    for i in my_lt_range(0, No_qij, 1):

        x = weighted_Q_norm
        y = matrix[:, i].astype(float)

        xbins = 100

        n, bin_edges = np.histogram(x, bins=xbins)
        sy, _ = np.histogram(x, bins=xbins, weights=y)

        mean = sy / n

        if i == 0:
            qij_Q = mean
        else:
            qij_Q = np.vstack((qij_Q, mean))
            
    qij_Q = np.transpose(qij_Q)
    # Insert Q edge in the first column;
    qij_Q = np.insert(qij_Q, 0, bin_edges[0:-1], axis=1)

    np.savetxt('qij_mean_Q.txt', qij_Q, fmt='%.3f')

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

    from findHistMin import findHistMin
    peakList = findHistMin();

    # Calculate the peak of the hist.txt, it will demarcate the TP state, not TS state!;

    print("The boundaries for the TP states are:")
    print(peakList)


############################################################################


if __name__ == "__main__":
    weightFile = sys.argv[1]
    qimapFile = sys.argv[2]

    calc_qij_Q(weightFile, qimapFile)
    print("When the voice of the Silent touches my words,")
    print("I know him and therefore know myself.")
