#!/bin/bash
#----------------------------------------------------
# Example SLURM job script to run MPI applications on 
# davinci system.
#
# Xingcheng Lin 07-08-2015, adapted from:
# $Id: job.mpi 1580 2013-01-08 04:10:50Z karl $
#----------------------------------------------------

#SBATCH --job-name=forPhivalue              # Job name
#SBATCH -o forPhivalue.%j.out       # Name of stdout output file (%j expands to jobId)
#SBATCH -e forPhivalue.%j.err       # Name of stderr output file;
#SBATCH --partition=commons
#SBATCH --nodes=1 --exclusive
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=60G
#SBATCH --time=24:00:00
#SBATCH --account=commons

# Launch the MPI executable named "a.out"
echo "I ran on:"
cd $SLURM_SUBMIT_DIR
echo $SLURM_NODELIST
#

#python phiValue_vanilla.py 65
python phiValue.py 12 6 57

