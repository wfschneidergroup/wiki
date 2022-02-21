#!/usr/bin/env python3

# Author: Jerry Crum

#When in the directory of a VASP job, running this script will show you the
#largest force acting on any single atom from the last iteration of your job.
#This will work while a job is still running, or when the job has completed.
#I find this helpful to use while a geometry optimization job is running,
#to know how close it may be to convergence. This script requires ASE
#(https://wiki.fysik.dtu.dk/ase/)

import os
import re
import numpy as np
from ase import Atoms
from ase.io import read

atoms = read('./POSCAR')
atoms = Atoms(atoms)
N = len(atoms)
f = open('./OUTCAR')
alllines=f.readlines()
f.close()
n = len(alllines)
for i in reversed(range(n)):
    line = alllines[i]
    if 'TOTAL-FORCE' in line:
        break
i+=2
forces = []
for atom in atoms:
    line = alllines[i]
    values = line.split()
    xforce = abs(float(values[3]))
    yforce = abs(float(values[4]))
    zforce = abs(float(values[5]))
    force = np.linalg.norm([xforce,yforce,zforce])
    forces.append(force)
    i+=1
fmax = max(forces)
print('Max force is {0} eV/A'.format(fmax))
