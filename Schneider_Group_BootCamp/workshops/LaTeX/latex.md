# Creating your first LaTeX project
Author: Craig Waitt
Date: 12/21/21

## Introduction

In the Schneider Group, we use a combination of Emacs/Org Mode and LaTeX to write our Outlines and Manuscripts. LaTeX is a powerful tool which seamlessly allows use to write mathematical equations as well as formats our atricle according to a journals specifications. I have created an open access Workshop that [covers the basics](https://github.com/cwaitt/Latex-Workshop) on how to use LaTeX as well as some exercises to help you practice. In this tutorial, we will go over the basic practice we follow in the Schneider Group on writing for publication [(also see the group wiki for a more detailed explaination)](https://github.com/wfschneidergroup/wiki/blob/master/Publishing.org). We will: 

1. Look at how to use emacs/org mode to create your first LaTeX document.

2. Create our first LaTeX template.

3. Learn how to compile and view your document.

## Setting up our Environment

For a detailed explaination on how the publication writing process works in the group, please click [here](https://github.com/wfschneidergroup/wiki/blob/master/Publishing.org). There are three stages in writing your first manuscript, Outlining, Iterative Drafts, and Supplemenatary Information. For each of these stages, we will create a template of sorts that you can use in your writing. Each of these templates will be written in a special version of emacs called **scimax**. Scimax is a very helpful emacs starterkit designed for people interested in reproducible research and publishing. Scimax is just emacs that has been configured extensively to make it act like we need it to for research documentation and publication. You can download scimax from Dr.Kitchin's github. Open a terminal session, log into the crc, and type the following:

```
git clone https://github.com/jkitchin/scimax.git
```

or my personal copy which has some different default settings to make life for us even easier.

```
git clone https://github.com/cwaitt/scimax.git
``` 

This will generate a folder in our home directory called **scimax**. Next, we need to configure our **.bashrc** file to enable scimax as well as LaTeX.

### The .bashrc File

Open your bashrc file with whichever text editor you prefer and add the following lines to it

```
#Additional aliases
alias scimax='~/scripts/scimax.sh' # This gives us a new command to open emacs as scimax

#Additional modules
module load emacs # this loads the crc version of emacs
module load texlive # this loads the crc version of LaTeX
```

Once you do that, exit your text editor and type:
```
source .bashrc
```

Nothing should appear to happen. 

Now create a new folder called *scripts* in your home directory, go into that folder, and type:
```
touch scimax.sh
```

This will create an empty file called **scimax.sh** 

Open **scimax.sh** with your favorite text editor and add the line:

```
#!/bin/bash
emacs -q -l /afs/crc.nd.edu/user/c/cwaitt/scimax/init.el $@
```

But change the *c/cwaitt* to your user first letter and username. This line is the command you would type to initialize scimax, however, earlier we told our **.bashrc** file that anytime we type the word scimax in the command line, that it should execute the command above.

Once you've made the appropriate changes, move to a new directory and create a file by typing.

** More content needed. Going back to do a tutorial on the bashrc file**


