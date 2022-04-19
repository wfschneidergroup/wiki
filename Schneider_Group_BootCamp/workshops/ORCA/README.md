# ORCA
Author: Craig Waitt

Date: 4/11/21

# Introduction

Our group primarily uses VASP, which is a DFT code that uses psuedo potentials and planewaves in order to do electronic and geometric minimizations, *ab initio* molecular dynamics, frequency calculations, etc. This tool is mostly designed to study surfaces and periodic systems. However, if you are interested in studying molecular systems, there are other tools that may be better suited. ORCA is one of those such tools. 

Orca is an *ab initio*, DFT, and semi-empirical package designed to do similar things as VASP, but for non-periodic systems. Rather than using planewaves, atomic orbitals are described using basis sets. It is open source (or you can just `module load orca`) and rather straight forward to use. This tutorial will go over the basic steps needed to create and run an orca job. You can also follow the directions presented [here](https://sites.google.com/site/orcainputlibrary/home?authuser=0). 

# Getting Started

Either in your .bashrc or in the command line, add/type:

```
module load orca
```

And you are ready to go. Whenever you want to run an ORCA job, you just type `orca` in the command line, followed by the input file (which we will create in a minute). You can also specify the parrallel version of orca by typing:

```
/afs/crc.nd.edu/x86_64_linux/orca/orca_4_0_1_2_linux_x86-64_openmpi202/orca
```

# Creating a Simple Input

An ORCA input is a single file called `{something}.inp`. Create a directory you want to start your own job, and type:

```
vi orca.inp
```

The **simple** input syntax, keywords are added in an order to the beginning with `!` or multiple lines of `!`:

```
! Keyword1 Keyword2 Keyword3 
```
or

```
! Keword1
! Keyword2
! Keyword3
```

You can also add comments using the `#` symbol.

The structure that you are doing the calculation on is in the same input as the parameters you want to use (unlike in VASP where each file is separate). This information is usually placed at the end of the input file. An example of a H2 molecule is shown below:

```
*xyz 0 1
H 0.0 0.0 0.0
H 0.0 0.0 1.0
*
```

Here the `*` starts and ends the coordinates of the H2 molecule. `xyz` lets orca know you are using cartesian coordinates, `0` is the charge of the system, and `1` is the spin multiplicity of the system. The following lines are each atom in the system followed by the cartesian coordinates in the x, y, and z directions. 

Lets say we want to do a geometry optimization on the H2 molecule using the PBE functional. Then the input would look something like this:

```
! PBE def2-SVP Opt 
# PBE is here the method (DFT functional), def2-SVP the basis set and Opt is the jobtype (geometry optimization). 
# Order of the keywords is not important.

*xyz 0 1
H 0.0 0.0 0.0
H 0.0 0.0 1.0
*
```

Now in the command line (or in a run script) you can type:

```
orca orca.inp > orca.out &
```

This will take a few moments to finish. and in the end you will have several output files.

```
-rw-r--r-- 1 cwaitt    217 Apr 11 16:17 orca.inp
-rw-r--r-- 1 cwaitt      4 Apr 11 16:17 orca.prop
-rw-r--r-- 1 cwaitt    167 Apr 11 16:17 orca.xyz
-rw-r--r-- 1 cwaitt   1022 Apr 11 16:17 orca.trj
-rw-r--r-- 1 cwaitt   4476 Apr 11 16:17 orca_property.txt
-rw-r--r-- 1 cwaitt   2883 Apr 11 16:17 orca.opt
-rw-r--r-- 1 cwaitt  76071 Apr 11 16:17 orca.gbw
-rw-r--r-- 1 cwaitt    402 Apr 11 16:17 orca.engrad
-rw-r--r-- 1 cwaitt 110563 Apr 11 16:17 orca.out
```

The files that we will look at are the orca.xyz, orca.trj, and orca.out.

## Structure files
`orca.xyz` contatins the final optimized coordinates of the H2 molecule. If you used the same parameters as above it should look like this:

```
2
Coordinates from ORCA-job orca
  H   0.00000000000000      0.00000000000000      0.11607770926261
  H   0.00000000000000      0.00000000000000      0.88392229073739
```

This is a xyz file and can be read by ase to visualize.

`orca.trj` is a trajectory file that shows the structure and energy (in hartree) at each step in the minimization:

```
2
Coordinates from ORCA-job orca E  -1.138965730007
  H       0.000000      0.000000      0.000000
  H       0.000000      0.000000      1.000000
2
Coordinates from ORCA-job orca E  -1.157803730897
  H       0.000000      0.000000      0.079377
  H       0.000000      0.000000      0.920623
2
Coordinates from ORCA-job orca E  -1.157337892070
  H       0.000000      0.000000      0.149988
  H       0.000000      0.000000      0.850012
2
Coordinates from ORCA-job orca E  -1.160582763351
  H       0.000000      0.000000      0.109390
  H       0.000000      0.000000      0.890610
2
Coordinates from ORCA-job orca E  -1.160683552662
  H       0.000000      0.000000      0.114749
  H       0.000000      0.000000      0.885251
2
Coordinates from ORCA-job orca E  -1.160687005395
  H       0.000000      0.000000      0.116131
  H       0.000000      0.000000      0.883869
2
Coordinates from ORCA-job orca E  -1.160687049941
  H       0.000000      0.000000      0.116078
  H       0.000000      0.000000      0.883922
```

This **is not** a xyz file and cannot be directly read by ase gui, but some manipulation of the file in python can be completed to visualize it in ase.

## The Output
The output file, `orca.out`, contains alot of information which I will not reproduce here. Similar to a VASP job, it will print/display the input parameters supplied and also the type of calculation that will be completed. It will then run through the SCF loop, gradient calculation in a cycle until convergence is met. You will get the forces on each atom as you would in VASP, as well as occupation or orbitals, population analysis, and total energy. If you go to the end of the file (around line 2366) you will see the words `*** Optimization Run Done ***`, above that is the total energy of the optimized H2 structure in Hartree (and if you keep scrolling up you will find the other properties mentioned), followed by the timing information. These calculations can be generated and read using ase to streamline data analysis, but we will not cover that here.

# More Complicated Input
Usually, we want to finely tune our calculations by adjusting some parameters, such as convergence criteria, adding dispersion, etc. To do that we use **blocks**. You cn think of blocks as advanced settings for different modules or keywords. A block starts with `%nameofblock` and ends with `end`. Things specified in **blocks** take precident over the simple input. I can repeat the same calculation as above but lets add the block to increase the maximum number of SCF steps to be 100. 

```
! PBE def2-SVP Opt 
# PBE is here the method (DFT functional), def2-SVP the basis set and Opt is the jobtype (geometry optimization). 
# Order of the keywords is not important.

%scf
MaxIter 100 # not really needed for this calculation but this is how you would write in a block
end

*xyz 0 1
H 0.0 0.0 0.0
H 0.0 0.0 1.0
*
```

For a complete list of blocks and the parameters you can adjust, see the ORCA manual [here](https://www.afs.enea.it/software/orca/orca_manual_4_2_1.pdf).

# Multiple Input
You can actually specify multiple jobs to be completed serially in a single input. 

Lets say, we wanted to optimize our structure with DFT, but then calculate the final energy using B3LYP.

```
! PBE def2-SVP Opt 
# PBE is here the method (DFT functional), def2-SVP the basis set and Opt is the jobtype (geometry optimization). 
# Order of the keywords is not important.

%base "pbeopt" # specifiles the root of the file (some blocks take a single word and do not need an end statement

*xyz 0 1
H 0.0 0.0 0.0
H 0.0 0.0 1.0
*

$new_job # starts a new job

! B3LYP def2-TZVP
# take the geometry from the previous job and recalculate the energy with a new functional and basis set
#
%base"b3lypsp"
```

When you look at `orca.out` you should see that it recognizes how many jobs are present and will start running through them serially. From the begining of the file to line 2451(ish), job 1 is being completed, then from there to the end of the file job 2 is being completed. This is very convienent for many situations, you can test a set of different electronic structure methods on the same structure, optimize a structure and immediately do vibrational calculations, and more.

# Some things to note

There is an art to selecting basis sets and adjusting parameters just like VASP. It will take practice before you can smoothly do these type of calculations. Additionally ASE has a calculator that allows you to visualize and extract data from an orca job, however it may not be a smooth as the VASP calculator. Finally, you are significantly limited to the number of atoms you can study in atom-centered basis codes, than compared to planewave based codes. Planewaves can be solved very quickly, where as basis sets are slower.
