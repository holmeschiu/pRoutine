#!/usr/bin/env python
# 
# Rename the file names after the drift correction from '---_2x_SumCorr.mrc'
# to just the name and number only. 
#
# 05/23/2014  Po-Lin Chiu
#

import os
import glob

dirName = "higher_dose/"
fileNameList = glob.glob(dirName+"*.mrc")

for nm in fileNameList:
    micNumber = nm[-19:-15]
    dstName = dirName + "fvccmplx_" + micNumber + ".mrc"
    os.rename(nm, dstName)

print "Done. "