#!/usr/bin/env python3

# Author Jerry Crum

from ase.io import read
import glob
from ase.visualize import view
import os
from ase import Atoms,Atom
import numpy as np

maxforces = []
folders = glob.glob('[0-9]'*2)
traj = []
energies = []
cwd = os.getcwd()
for f in folders:

    #Get the length of atoms, and last image from OUTCAR
    atoms = read('{}/OUTCAR'.format(f))
    traj+=[atoms]
   
    #Move through the image directories
    os.chdir(f)

    # Get forces
    fmax = 0 #incase there are is not a force listed for the initial or final state
    f2 = os.popen('grep FORCES: OUTCAR | tail -1')
    for line in f2:
        fields = line.split()
        fmax = float(fields[4])

    maxforces.append(fmax)

    # Get energies
    o = open('./OUTCAR')
    alllines = o.readlines()
    o.close()
    n = len(alllines)

    for i in reversed(range(n)):
        line = alllines[i]
        if 'energy(sigma->0)' in line:
            break
    fields = line.split()
    energies.append(fields[-1])


    # Go back to main directory
    os.chdir(cwd)
energies =np.array(energies)
energies = energies.astype(float)
nenergies = energies - energies[0]
print('Image \t | FMax \t | Energy \t | Rel. En.')
print('----------------------------------------------------')
for i,f,e,ne in zip(folders,maxforces,energies,nenergies):
    print('{0} \t | {1:.4f} \t | {2:.4f} \t | {3:.4f}'.format(i,f,e,ne))
view(traj)
