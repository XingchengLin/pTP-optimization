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

    No_qij = np.shape(matrix)[1]

    for i in my_lt_range(0, No_qij, 1):

        x = weighted_Q_norm
        y = matrix[:, i].astype(float)

        xbins = 50

        n, bin_edges = np.histogram(x, bins=xbins)
        sy, _ = np.histogram(x, bins=xbins, weights=y)

        mean = sy / n

        if i == 0:
            qij_Q = mean
        else:
            qij_Q = np.vstack((qij_Q, mean))
            
    qij_Q = np.transpose(qij_Q)
    # Insert Q edge in the first column;
    print(np.shape(qij_Q))
    print(bin_edges[0:-1])
    qij_Q = np.insert(qij_Q, 0, bin_edges[0:-1], axis=1)

    np.savetxt('qij_mean_Q.txt', qij_Q, fmt='%.3f')


############################################################################


if __name__ == "__main__":
    weightFile = sys.argv[1]
    qimapFile = sys.argv[2]

    calc_qij_Q(weightFile, qimapFile)
    print("When the voice of the Silent touches my words,")
    print("I know him and therefore know myself.")
