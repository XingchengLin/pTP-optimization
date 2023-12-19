# pTP-optimization
Scripts for doing pTP-optimization of reaction coordinate

*To initiate the command, you should have a qimap.out file listing all the binary formation of each of the protein contacts. After that, you can just do:

```
python2.7 main_ini.py
```

*Note, you also need to replace the optimize.py file in the folder anaconda2/lib/python2.7/site-packages/scipy/optimize/ with the file provided in this folder, if you want to use the "Downhill Simplex" method

## Reference:
* Work: https://research.wmz.ninja/articles/2018/03/on-sharing-large-arrays-when-using-pythons-multiprocessing.html
* Not working: http://briansimulator.org/sharing-numpy-arrays-between-processes/
* Not working: https://pypi.org/project/SharedArray/
