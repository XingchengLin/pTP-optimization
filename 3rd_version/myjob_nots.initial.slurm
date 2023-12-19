#!/bin/bash
#----------------------------------------------------
# Example SLURM job script to run MPI applications on 
# davinci system.
#
# Xingcheng Lin 07-08-2015, adapted from:
# $Id: job.mpi 1580 2013-01-08 04:10:50Z karl $
#----------------------------------------------------

#SBATCH --job-name=prionOpt              # Job name
#SBATCH -o prionOpt.%j.out       # Name of stdout output file (%j expands to jobId)
#SBATCH -e prionOpt.%j.err       # Name of stderr output file;
#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=60G
#SBATCH --time=24:00:00
#SBATCH --account=commons

module purge
module load icc/2015.2.164 OpenMPI/1.8.6

# Launch the MPI executable named "a.out"
echo "I ran on:"
cd $SLURM_SUBMIT_DIR
echo $SLURM_NODELIST
#

$HOME/bin/anaconda2/bin/python main_ini.py


