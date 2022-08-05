#!/usr/bin/env python

import os, sys, time, random

root = hash(os.path.basename(os.getcwd()))
random.seed()

cputime = float(root % 50) / 10 + random.random() * 0.2
perftime = float(root % 42) + random.random() * 4
memory = float(root % 500) + random.random() * 10

print "Starting a long and memory consuming process..."
sys.stdout.flush()
while 1:
    if time.clock() >= cputime:
        break

print("Wallclock time loading from the database:", round(perftime, 2), "seconds.")
print(round(memory, 2), "MB of RAM was the peak memory.")
print("End")
