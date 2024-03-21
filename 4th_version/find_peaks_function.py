###########################################################################
# This script will help find the peaks of histQ.txt;
# 
# Written by Rushi Faldu, 03/7/2024;
###########################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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

# Defining a function to find the peaks
def find_peaks_function ():

    # Loading data from the histQ.txt file
    data = np.loadtxt('histQ.txt')

    # Extracing X and Y data for the graph
    x = data[:, 0]
    y = data[:, 1]

    # Convert to numpy array
    x = np.array(x)
    y = np.array(y)

    # Finding the peaks
    peaks,_ = find_peaks(y, distance=50)

    print("peak_index =", peaks)

    # Plotting the graph
    peak_x_values = [x[i] for i in peaks]
    peak_y_values = [y[i] for i in peaks]

    print("peak x values =",peak_x_values)
    print("peak y values =",peak_y_values)

    plt.plot(x,y)
    plt.scatter(peak_x_values, peak_y_values,marker='x', color='red', label='Peaks')

    plt.show()

    return peak_x_values
