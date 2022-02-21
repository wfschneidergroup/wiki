# Author Jerry crum

from ase import Atoms, Atom
import numpy as np
from ase.io import write, read
from ase.neb import NEB
from ase.visualize import view

r = read('00/OUTCAR')   # Path to reactants OUTCAR
p = read('07/OUTCAR')   # Path to products OUTCAR
view(r)
view(p)
pr = r.get_positions()  # Reactants position list
pp = p.get_positions()  # Products positions list

cell = r.get_cell()  # Gets the matrix which defines the supercell

# Calculated the difference in postions from reactants to products
# If any atoms are more than half the supercell away from their
# starting position, this code will wrap/unwrap them.
diff = pr-pp
for i,d in enumerate(diff):
    d = abs(d)
    index = np.argsort(d)
    index = index[::-1]
    for j in index:
        if abs(d[j]) > np.linalg.norm(cell[j])/2:
            if pr[i][j] < np.linalg.norm(cell[j])/2:
                pr[i] += cell[j]
            elif pr[i][j] > np.linalg.norm(cell[j])/2:
                pr[i] -= cell[j]
            d = abs(pr[i]-pp[i])
            diff = pr-pp

# This section checks the distancs after unwrapping to make sure all atoms are
# less than half the supercell away from their starting position
diff2 = pr-pp
for i,d in enumerate(diff2):
    if abs(d[0])>np.linalg.norm(cell[0])/2 or abs(d[1])>np.linalg.norm(cell[1])/2 or abs(d[2])>np.linalg.norm(cell[2])/2:
        print(i,p[i].index,d)
        print('pr = ',pr[i])
        print('pp = ',pp[i])

# Now that all the positions are fixed, assign the positions to the Reactants
r.set_positions(pr)
view(r)
images = [r]
images += [r.copy() for i in range(4)]
images += [p]

neb = NEB(images)
neb.interpolate('idpp')

# view(images)
# create directory and files or submist an NEB calc using ase 
