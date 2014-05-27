#!/usr/bin/env python

from EMAN2 import *
from sparx import *

s = 64. / 256.
fiL = "fpctfStack.hdf"

for i in xrange(n):
    a = get_im(fiL, i)
    b = resample(a, s)
    b.write_image("bdb:reduced_fvcc", i)

print "Done. "
