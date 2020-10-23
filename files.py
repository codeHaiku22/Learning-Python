#!/usr/bin/python3

#File Handling
"""
The key function for working with files in Python is the open() function.
open(<filepath>, [mode][text/binary])

There are 4 different methods/modes for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition, you can specify if the file should be handled in binary or text mode:
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

#Open a File
#open()
#To open a file just for reading, it is enough to specify simply the name of the file
f = open("demofile.txt")

#This is the same as
f = open("demofile.txt", "rt")

#If a file does not exist, an error will be generated
#f = open("ljflsajflsaf.txt")                    #FileNotFoundError: [Errno 2] No such file or directory: 'ljflsajflsaf.txt'

#read()
#The open() function returns a file object, which has a read() method for reading the content of the file.
f = open("demofile.txt", "r")

print(f.read())                                 #Hello!  Welcome to demofile.txt.
                                                #This file is for testing purposes.
                                                #Good luck!

#The read() method can also be used to return specific characters of text
f = open("demofile.txt", "rt")

print(f.read(5))                                #Hello

#readline
#Returns onle line of txt
f = open("demofile.txt")

print(f.readline())                             #Hello!  Welcome to demofile.txt.

#By calling readline() again, you can read the next line.
f = open("demofile.txt")

print(f.readline())                             #Hello!  Welcome to demofile.txt.
print(f.readline())                             #This file is for testing purposes.

#By looping through the lines of the file, you can read the while file, line by line.
f = open("demofile.txt")

for x in f:
    print(x)                                    #Hello!  Welcome to demofile.txt.
                                                #This file is for testing purposes.
                                                #Good luck!
#Close Files
#close()
#It is good practice to always close the file when you are done with it.
f = open("demofile.txt")

f.close()

