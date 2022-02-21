#!/usr/bin/env python3

# Author Jerry Crum

import os
import numpy as np
import math

f = os.popen('qstat -f -U $USER -q *@@schneider',"r")
usedt = 0
totalt = 0
freet = 0
print('-----------------------------------------------')
print('Node \t\t Cores \t Used \t Free \t Status')
print('-----------------------------------------------')
for line in f:
    if 'PENDING JOBS' in line:
        break
    if 'long' in line:
        fields = line.split()
        node = fields[0]
        node = node.rstrip('.crc.nd.edu')
        node = node.lstrip('long@')
        cores = fields[2]
        z = cores.split('/')
        total = int(z[2])
        used = int(z[1])
        free = total - used
        totalt += total
        usedt += used
        freet += free
        if len(fields)>5:
            print('{0} \t {1} \t {2} \t {3} \t {4}'.format(node,total,used,free,fields[5]))
        else:
            print('{0} \t {1} \t {2} \t {3}'.format(node,total,used,free))
print('-----------------------------------------------')
print('Total \t\t {0} \t {1} \t {2}'.format(totalt,usedt,freet))
print('-----------------------------------------------')
print('###############################################')

f = os.popen('qstat -f -U $USER -q *@@schneider',"r")
qlines = []

alllines=f.readlines()
for i,line in enumerate(alllines):
    if 'long' in line:
        qlines.append(i)
    if '#####' in line:
        qlines.append(i)
        break
n = len(qlines)
user = []
cores = []
for i in range(n-1):
    job = np.arange(qlines[i]+1,qlines[i+1]-1)
    for t in job:
        fields = alllines[t]
        fields = fields.split()
        user.append(fields[3])
        cores.append(fields[7])
uni = np.unique(user)
total_cores=[]
for x in uni:
    s=0
    for i,u in enumerate(user):
        if u == x:
            s+=int(cores[i])
    total_cores.append(s)

total_cores=np.array(total_cores)
percent = total_cores/totalt*100
s_percent = sum(total_cores/totalt*100)
s_cores = sum(total_cores)
print('-----------------------------------------------')
print('User \t  Cores Used \t  Percent of all cores')
print('-----------------------------------------------')
for u,c,p in zip(uni,total_cores,percent):
    print('{0} \t |\t {1} \t |\t {2:.0f}\t%'.format(u[0:6],c,p))
print('-----------------------------------------------')
print('Totals \t |\t {0} \t |\t {1:.0f}\t%'.format(s_cores,s_percent))
print('-----------------------------------------------')
