# pTP-optimization
script for doing pTP-optimization of reaction coordinate

To initiate the command, you should have a qimap.out file listing all the binary formation of each of the protein contacts. After that, you can just do:

python2.7 main_ini.py


Note, you also need to replace the optimize.py file in 
anaconda2/lib/python2.7/site-packages/scipy/optimize/

with the file provided in this folder, if you want to use the "Downhill Simplex" method
