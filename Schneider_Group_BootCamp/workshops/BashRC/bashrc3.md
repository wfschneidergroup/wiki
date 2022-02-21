# Modules
Author: Craig Waitt
Date: 01/15/22

## Introduction
The CRC systems have preloaded software which is not included within a standard build of your asf account. You can easily install these software through the `module` command.

## The Module Command
To see all availible modules, type in the command line:

```
module avail
```

To see a specific module:

```
module avail XYZ
```

When you log in, you can set some modules to load automatically in your bashrc file by using the `module load` command. Here are a few modules that you may find helpfull.

```
#Additional modules
module load emacs   # emacs text editor
module load git     # version control, used to push and pull from GitHub
module load texlive # Latex Packages
module load vasp    # VASP (restricted software)
module load mathematica # Mathematica
module load matlab  # Matlab
module load vim     # Vim text editor
module load python/3.7.3 # python library
module load orca    # Atoms centered Basis DFT and HF code
```

You can always remove a module through the `module unload` command. Word of warning, Anaconda causes some issues with Fastx. As such, I suggest using the CRCs version of python. Others may have different opinions. 

[<<< Intro](README.md)

[<<< Alliases](bashrc2.md)

[Paths >>>](bashrc4.md)

