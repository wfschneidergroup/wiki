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


