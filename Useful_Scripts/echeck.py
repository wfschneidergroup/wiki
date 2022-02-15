#!/usr/bin/env python3

# Author Jerry Crum

import os
import numpy as np
import matplotlib.pyplot as plt

f = os.popen('grep "free  energy" OUTCAR')
energy = []
for line in f:
    fields = line.split()
    energy.append(float(fields[4]))

n = len(energy) -1
ediff = []
x = []
for i in range(n):
    x.append(i)
    ediff.append(abs(energy[i+1]-energy[i]))


f = os.popen('grep "FORCES:" OUTCAR')
fmax = []
for line in f:
    fields = line.split()
    fmax.append(float(fields[4]))
    

list = np.arange(n-5,n)
print('------------------------------------------------------')
print('Iter \t | fmax \t | E[i]-E[i-1]')
print('------------------------------------------------------')
for i in list:
    print('{0} \t | {1:0.4f} \t | {2:0.3E}'.format(i,fmax[i],ediff[i]))
    
#plt.plot(x,ediff)
#plt.show()
    
