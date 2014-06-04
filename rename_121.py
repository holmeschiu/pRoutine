#!/usr/bin/env python
# Make a subdirectory "arranged/" first. 

import os
import glob
import shutil

filelist = glob.glob("*.dm3")
if os.path.isfile("filelist.txt"): 
    flog = open("filelist.txt", 'r').readlines()
    orifile_num = len(flog)
    orifile = []
    for line in flog:
        orifile.append(line.split()[0])
else:
    orifile = []
    orifile_num = 0

if os.path.isfile("temp1345.txt"):
    os.remove("temp1345.txt")
fw = open("temp1345.txt", 'w')

start = orifile_num + 1
for f in filelist:
    b = os.path.basename(f)

    if b not in orifile:
        angle = b[:2]
        micnumber = b[-7:-4]
    
        dstname = "%s%04d.dm3" % (angle, start)
        start = start + 1
    
        print "%30s  -->  %s" % (b, dstname)
        fw.write("%30s  -->  %s\n" % (b, dstname))

        shutil.copyfile(b, "arranged/"+dstname)
    else:
        print "%s has already renamed. " % b
        fw.write(flog[orifile.index(b)])
        continue

fw.close()
if os.path.isfile("filelist.txt"): 
    os.remove("filelist.txt")
os.rename("temp1345.txt", "filelist.txt")
print "Done. "