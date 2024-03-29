####################################################################################
# This script will help calculate the pTPr according to Gerhard Hummer's Bayesian 
# formula; It has been compressed into a f function;
#
# Written by Xingcheng Lin, 12/12/2016
####################################################################################

import subprocess;
import os;
import shutil;
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
###########################################

# Load data from Q.out using numpy
data_Q = np.loadtxt("Q.out")

# Extract the second column
values_Q = data_Q[:,1]

# Check if all values are between 0 and 1
if not np.all((values_Q >= 0) & (values_Q <= 1)):

    # Find the maximum value
    max_Q = np.max(values_Q)

    # Normalize the second column
    normalized_values_Q = values_Q/max_Q

    # Combine the normalized values into a new array
    normalized_Q = np.column_stack((data_Q[:,0], normalized_values_Q))

    # Save the normalized data to Q_normalized.out
    np.savetxt('Q_normalized.out', normalized_Q, fmt=['%0.6f','%0.12f'])
    
else:
    np.savetxt('Q_normalized.out', data_Q, fmt=['%0.6f','%0.12f'])

###########################################
def function():

    # Calculate the free energy plot;
    topRC = 1.0;
    bottomRC = 0.0;
    stepRC = 0.01; # We decided to have 100 number of bins;
    inputName = "Q_normalized.out";
    output1Name = "histQ.txt";
    output2Name = "histQ_smooth.txt";
    output3Name = "FvQ.txt";

    paramList = [topRC, bottomRC, stepRC, inputName, output1Name, output2Name, output3Name];

    from fenergy import fenergy
    fenergy( paramList );

    from find_peaks_function import find_peaks_function
    peakList = find_peaks_function();

    print ("peakList =",peakList);

    # Calculate for Transition path ensemble;
    from findTP import findTP
    findTP( peakList );

    # Sort according to the first column so that the time will keep increasing;
    # This is because findTP.py does not output in a increasing-time manner;
    subprocess.call("sort -s -n -k 1,1 TPtime.xvg > TPtime.sort.xvg", shell=True);

    # Get QTP files;
    subprocess.call("paste Q_normalized.out TPtime.sort.xvg | awk '{if($4==1)print $1,$2}'>QTP.out", shell=True);

    # Calculate Q for TP.xtc

#    # Calculate p(TP);
    no = float(subprocess.check_output("wc -l Q_normalized.out | awk '{print $1}'", shell=True))
    no_TP=float(subprocess.check_output("wc -l QTP.out | awk '{print $1}'", shell=True));

    print ("p(TP) =",no, no_TP);

#    # Calculate P(r) and P(r|TP);
    inputName = "QTP.out";
    output1Name = "histQ_TP.txt";
    output2Name = "histQ_TP_smooth.txt";
    output3Name = "FvQ_TP.txt";

    paramList = [topRC, bottomRC, stepRC, inputName, output1Name, output2Name, output3Name];
    fenergy( paramList );

    # Finally, invoke the Bayesian equation to evaluate P(TP|r);
    subprocess.call("paste histQ_TP.txt histQ.txt | awk -v var1='%d' -v var2='%d' '{if($4 != 0)print $1,$2*var2/var1/$4}'>pTPr.txt" %(no, no_TP), shell=True)

    # Take the largest number of pTPr and return;
    infile = open("pTPr.txt", "r");
    matrix = [line.strip().split() for line in infile];
    infile.close();
    length = len(matrix);
    maxPTPr = 0.0;

    for i in my_lt_range(0, length, 1):
        tmp = float(matrix[i][1]);
        if (tmp > maxPTPr):
            maxPTPr = tmp;
           
    print ("maxPTPr =",maxPTPr);
    return maxPTPr;

############################################################################

if __name__ == "__main__":

    function()

    print("The song I came to sing")
    print("remains unsung to this day")

