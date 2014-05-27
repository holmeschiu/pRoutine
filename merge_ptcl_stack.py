#!/usr/bin/env python

import os

from EMAN2 import *

prtl_stack_prefix = "windows/ptcl_fvccmplx_"
output_total_stack = "total.hdf"
total_num_prtc = 0

if os.path.isfile(output_total_stack): os.remove(output_total_stack)

for ptcl_i in range(9999):
    dst_ptcl_stack = "%s%04d.hdf" % (prtl_stack_prefix, ptcl_i+1)

    if os.path.isfile(dst_ptcl_stack):
        num_prtc = EMUtil.get_image_count(dst_ptcl_stack)
        a = EMData()
        a.read_images(dst_ptcl_stack)

        for n in range(num_prtc):
            a[n].write_image(output_total_stack, -1)

        total_num_prtc += num_prtc
    
    else:
        continue

print "Total particle number is %d.  Done. " % total_num_prtc

