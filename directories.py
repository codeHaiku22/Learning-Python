#!/usr/bin/python3

#Iterate Over Files in a Directory
#There are multiple methods that can be used to loop through the contents of a directory.

#METHOD #1
#os.listdir()
"""
This method returns a list containting the names of the entries in the directory.
 - The list is in arbitrary order and does not include the special entries "." and "..".
"""
print("\n###[ os.listdir() method ]##########################################################################")
import os

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

for filename in os.listdir(directory):
    if filename.endswith(".py") or filename.endswith(".txt"):
        print(os.path.join(directory, filename))
    else:
        continue

#METHOD #2
#os.scandir()
"""
Since Python 3.5, things are much easier with os.scandir().
This method is similar to os.listdir().
"""
print("\n###[ os.scandir() method ]##########################################################################")
import os

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

for entry in os.scandir(directory):
    if entry.path.endswith(".py") or entry.path.endswith(".txt") and entry.is_file():
        print(entry.path)

#METHOD #3
#os.walk()
"""
This method will iterate over all descendant files in subdirectories.  
Consider the os.scandir() example, but in this case, this method recursively prints all files in the directory.
"""
print("\n###[ os.walk() method ]#############################################################################")
import os

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

for subdir, dirs, files, in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".py") or filepath.endswith(".txt"):
            print(filepath)

#METHOD #4
#glob
"""
The glob module finds all the pathnames matching a specified pattern according to the rules used by the UNIX shell.
 - Results are returned in arbitrary order.
"""
print("\n###[ glob module ]##################################################################################")
import glob

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

for filepath in glob.iglob(directory + "/*.py"):
    print(filepath)

for filepath in glob.iglob(directory + "/*.txt"):
    print(filepath)

#By default, glob.iglob only lists files immediately under the given directory.
#To recursively list all files in nested folders, set the recursive parameter to True.
import glob

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

for filepath in glob.iglob(directory + "/*.py", recursive=True):
    print(filepath)

for filepath in glob.iglob(directory + "/*.txt", recursive=True):
    print(filepath)

#Note: You can either use glob.iglob or glob.glob to return entries which yield the paths matching a pathname pattern:
#       - glob.iglob returns an iterator
#       - glob.glob returns a list

#METHOD #5
#The code below does the same as the example above, by using a different module and method.
print("\n###[ pathlib.Path() method ]########################################################################")
import pathlib

directory = "/mnt/c/Users/dgrewal/Documents/Projects/Development/_git/Learning-Python"

paths = pathlib.Path(directory).glob('**/*.py')

for path in paths:
    path_in_str = str(path)
    print(path_in_str)