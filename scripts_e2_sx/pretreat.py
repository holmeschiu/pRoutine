#!/programs/local/x86_64-linux/tw/eman2/20140325/extlib/bin/python

import glob

from EMAN2 import *

param_dict = {}
dirName = "higher_dose/"
inImage = glob.glob(dirName+"*.mrc")

for im in inImage:
    imNumber = im[-19:-15]
    outImage = dirName + "medfvccmplx_" + imNumber + ".mrc"

    a = EMData(im)
    b = a.process("eman1.filter.median", {"radius":3})
    b.process_inplace("normalize.edgemean")
    b.write_image(outImage)

print "Done. "


