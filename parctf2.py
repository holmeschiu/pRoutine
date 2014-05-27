#!/usr/bin/env python
#
#
#   Presumed naming format: 
#       Particle stack for each micrograph -- 
#           Working on MRC first for the script. 
#
#       Numbering --
#           4 digits for micrographs
#                                              
#   
# Po-Lin Chiu  05/25/2014

import os
import sys
import re

from EMAN2 import *
from sparx import *

inCTFList = "ctfs.txt"                                   # output text list from sxcter.py
outStack = "ctfStack.hdf"                                # output total particle stack

# Read the CTF parameter list
ctfList = read_text_row(inCTFList)

# Find the corresponding number in each micrograph and the stack of total particles
acumNumbPrtc = 0

if os.path.isfile("parlist.txt"):       os.remove("parlist.txt")
if os.path.isfile(outStack):            os.remove(outStack)

fparlist = open("parlist.txt", 'w')

# Make a file list from the particle stack of each micrograph (fprtcStckList). 
ptcl_root = "windows/iptcl_fvccmplx_"
ptcl_sufx = ".hdf"
fprtcStckList = []
for s in xrange(9999):
    dstfilename = "%s%04d%s" % (ptcl_root, s+1, ptcl_sufx)
    if os.path.isfile(dstfilename):
        fprtcStckList.append(dstfilename)

for fs in fprtcStckList:
    # Read the particle numbers from the particle stacks
    numPrtc = EMUtil.get_image_count(fs)    # particle number of each image for the format other than MRC
    
    # Write CTF parameters in the particle header
    micgi = re.findall(r'\d+', fs)[0]

    for n in xrange(len(ctfList)):
        if micgi in str(ctfList[n][-1]):
            indxMicgInCTFList = n
        else:
            continue

    for prtci in xrange(numPrtc):
        b = get_im(fs, prtci)
        b.set_attr("ctf", generate_ctf(ctfList[indxMicgInCTFList][:9]))
        prtcii = acumNumbPrtc + prtci
        b.write_image(outStack, -1)
        
        print "Particle #%06d: " % prtcii
        print ctfList[indxMicgInCTFList][:9]
        
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = ctfList[indxMicgInCTFList][:9]
        
        writeLine = "%6d   %s   %9.5f   %4.2f   %4.1f   %8.3f   %7.2f   %8.4f   %9.6f   %9.5f   %8.6f\n" % (prtcii, fs, c1, c2, c3, c4, c5, c6, c7, c8, c9)
        fparlist.write(writeLine)

    acumNumbPrtc += numPrtc
    
prtcNumber = acumNumbPrtc
fparlist.close()

print "\n%d total particle have been processed.  Done. " % prtcNumber

