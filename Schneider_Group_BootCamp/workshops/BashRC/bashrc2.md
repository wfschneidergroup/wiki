# Aliases
Author: Craig Waitt
Date: 01/7/22

## Introduction
Sometimes typing commands can get very repetitive, or if you need to type a long command many times, it is best to have an alias you can use for that. To create an alias for a command, you simply need to specify an alias name and set it to the command.

```
alias custom_name='command to execute'
```

When you open a terminal, your bashrc file will execute/activate your aliases. You should add these aliases, or modify them to your liking.

```
#Additional aliases
alias ls='ls -FG --color=auto' ## The traditional ls command but adds colors to distiguish between files,directories, and scripts.
alias ll='ls -lrt --color=auto' ## Same as above except it displays file information vertically
alias rm='rm -f' ## ignore nonexistent files and arguments (be careful!!!)
alias follow='tail -f' ## opens and follows the progress of a file live (ex: watch the OUTCAR as it optimizes the electronic structure of a system)
alias check='qstat -u $USER' ## checks the status of your qued and running calculations (replace $USER with your own user name)
alias qcheck='qstat -f -q *@@schneider' # check the status of the schneider nodes
alias mystat="qstat -u cwaitt -xml | tr '\n' ' ' | sed 's#<job_list[^>]*>#\n#g' | sed 's#<[^>]*>##g' | grep ' ' | column -t" # more detailed version of check alias
alias dftfe='ssh -Y $USER@$FRONTEND.crc.nd.edu' ## ssh log into a CRC frontend (replace $USER and $FRONTEND appropriately)
alias jpn='jupyter notebook'

## Some more specific aliases for other software
alias orca_par='/afs/crc.nd.edu/x86_64_linux/orca/orca_4_0_1_2_linux_x86-64_openmpi202/orca' #for a parallel ORCA calculation
alias pycharm='sh ~/PyCharm/pycharm-community-2021.1.3/bin/pycharm.sh' for a pycharm calculation
```

You can always remove an aliase during your current session by typing `unalias custome_name`

There are more aliases you can add such as 'ssh login' or 'cd to your scratch 365 directories'. You can add aliases for a wide variety of purposes an should to help streamline your work.

[<<< Intro](README.md)

[Modules >>>](bashrc3.md)

