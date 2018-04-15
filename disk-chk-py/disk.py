#!/usr/bin/python
import os
os.system("df -Th 1> /root/disk.txt")
fp=open("/root/disk.txt")
#print x
y=fp.readlines()
x=""
for i in y:
        if i.startswith("/"):
                x=i.split()[0]+"  mount on  "+i.split()[-1]+"  disk usages  "+i.split()[-2]

print x

