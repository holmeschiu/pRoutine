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
# Po-Lin Chiu  04/11/2014

from EMAN2 import *
from sparx import *
import os, sys, glob

inCTFList           = "ctfs_8x.txt"                      # output text list from sxcter.py
inPtrcStckRootName  = "prtcStacks/s_"                    # input particle file root name
extension           = "hdf"                              # file format of the particle image
outStack            = "totalStack.hdf"                   # output total particle stack

# Read the CTF parameter list
ctfList = read_text_row(inCTFList)

# Find the corresponding number in each micrograph and the stack of total particles
acumNumbPrtc = 0

if os.path.isfile("parlist.txt"):       os.remove("parlist.txt")
if os.path.isfile(outStack):            os.remove(outStack)

fparlist = open("parlist.txt", 'w')

fprtcStckList = glob.glob(inPtrcStckRootName+"*"+"."+extension)

for fs in fprtcStckList:
    # Read the particle numbers from the particle stacks
    if extension == "mrc":
        a = get_im(fs)
        
        nx = a.get_xsize()
        ny = a.get_ysize()
        nz = a.get_zsize()
        
        for i in xrange(nz):
            sli = Util.window(a, nx, ny, 1, 0, 0, i-nz//2)
            sli.write_image(fs[:-4] + ".hdf", i)
        
        numPrtc = nz
    else:
        numPrtc = EMUtil.get_image_count(fs)    # particle number of each image for the format other than MRC
    
    # Write CTF parameters in the particle header
    micgi = fs[-8:-4]                           # read the particle stack number
    
    for n in xrange(len(ctfList)):
        if micgi in str(ctfList[n][-1]):
            indxMicgInCTFList = n
        else:
            continue
    
    for prtci in xrange(numPrtc):
        if extension == "mrc": 
            b = get_im(fs[:-4] + ".hdf", prtci)
        else:
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

