# The .bashrc File
Author: Craig Waitt
Date: 12/21/21

## Introduction
There are many different types of shells which can be used by the Linux terminal. A shell is a command line interpeter (think of it as the same as the difference between python and java). It provides an interface between the user and the kernel and executes programs called commands (the kernel is another term for operating system). When you create a CRC account, your default shell is set to BASH (Bourne-Again Shell). When you buy a new macbook, your default shell is Zsh. Once you log into the CRC, several login scripts are run which load a user's personal preferences. One these such scripts is called the **.bashrc**. Upon creation of your account, the **.bashrc** file with default setting is copied into a users home directory. The user can then modiy that file to customize their session. They can modify environment variable, load modules, create aliases, and many many other things. In this tutorial, we are going to cover how a typical **.bashrc** file is configured. These settings can be changed to your liking. Please be cautious as improper formating in your **.bashrc** file can cause some very basic commands, such as ls or mv, not work.

## Editing your .bashrc
To edit your **.bashrc** you only need to be in your home directory. The group uses a variety of text editors such as emacs, vi, and nano. I will be using vi's cousin vim, but feel free to use which ever one you are most comfortable with. Some of the saving and exit commands will be different but the editing of the **.bashrc** will be the same.

To begin, log into the CRC and open your **.bashrc** file by typing:

```
vim ~/.bashrc
```

`vim` is the text editor I am using, `~` is a bash short cut to typing the path of my home directory (/afs/crc.nd.edu/user/c/cwaitt), and `/.bashrc` is the files I want to edit.

your should be greated with a fairly blank/empty file that looks like this:

```
#Check http://crc.nd.edu/wiki for login problems
#Contact crcsupport@nd.edu if further problems

if [ -r /opt/crc/Modules/current/init/bash ]; then
        source /opt/crc/Modules/current/init/bash
fi

if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

##Additional aliases

##Additional modules
```

In a bash shell session, comments are denoted with a `#` symbol. So in your CRC's **.bashrc** file, you have several comments followed by two if statements. The first is checking for the CRC modules that you can load, and the second is checking for systme wide function and aliases the CRC has created. **DO NOT TOUCH THESE LINES UNLESS YOU KNOW WHAT YOU ARE DOING**. In the next sections We will discuss how to add/create aliases and modules. Then we will cover what a path is and how to set a path.

[Alliases >>>](./bashrc2.md)

[Modules >>>](./bashrc3.md)

[Paths >>>](./bashrc4.md)

