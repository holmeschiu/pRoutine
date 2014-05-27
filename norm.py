#!/usr/bin/env python

import os

from EMAN2 import *
from sparx import *

stack_root = "ptcl_fvccmplx_"
stack_sufx = ".hdf"

stack_list = []
for n in range(9999):
    dstfilename = "%s%04d%s" % (stack_root, n, stack_sufx)
    if os.path.isfile(dstfilename):
        stack_list.append(dstfilename)

refmask = EMData("maskfile.hdf")
for fs in stack_list:
    num_prtc = EMUtil.get_image_count(fs)

    out_stack_name = "i%s" % fs
    if os.path.isfile(out_stack_name): os.remove(out_stack_name)
    for i in xrange(num_prtc):
        a = get_im(fs, i)
        st = Util.infomask(a, refmask, False)  
        b = ramp((a-st[0]) / (-st[1])) 
        b.write_image(out_stack_name, i)  

print "Done. "
