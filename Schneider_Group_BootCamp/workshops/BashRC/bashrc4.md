# Paths
Author: Craig Waitt
Date: 01/15/22

## Introduction
You will often write your own scripts or download external codes that you want to execute. You can always reach out the the CRC for assistance. Here, we will cover how to use a script written by Jerry Crum, and set it on your path so you can execute the script where ever you are.

## The nodestats.py script
You should have a set directory to store all your scripts that you want to use. In your home directory, make a folder called `scripts`.

```
mkdir ~/scripts
```

There is a folder in the Schneider Group Folder called [Useful Scripts](../../../../Useful_Scripts). Copy the nodestats.py script from here into your `scripts` directory. 

Open your bashrc file and add the folloing lines of code.

```
# Personal Scripts
export PATH=~/scripts/:$PATH
```

$PATH is a variable that contains the path (or direction) to executable files on your system. Two things to note:

1. The `$` is used to declare variables in bash. If you forget the `$` symbol in the above lines of code, you can mess up your path and the command line will stop working. Commands like `rm` and `mkdir` will stop working all together. If that happens you need to reach out to someone who can fix it.

2. The way the export command is written, it will append the path to the scripts folder ahead of your path, which means when you execute a command the computer will look in your scripts folder first, then other things in your path. If you wanted to put the `scripts` folder at the end of your path, you would write `export PATH=$PATH:~/scripts/`. This may have an impact of certain scripts that depend on other things.

Now, any script you place in this folder is executable from any location/folder you are in. You can execute the script by typing `nodestats.py` (or add an aliase to change the command).

Feel free to add any script in the [Useful Scripts](../../../../Useful_Scripts) folder or add your own!

## Conclusion

In this session, we covered how to configure your **.bashrc** file to optimize your work. We covered how to create aliases, load modules, and set your path. [Linux Journey](https://linuxjourney.com/) is an excellent source that covers Linux commands and the structure of the Linux architecture.

[<<< Intro](./README.md)

[<<< Modules](./bashrc3.md)
