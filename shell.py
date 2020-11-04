#!/usr/bin/python3

#Executing Shell Commands with Python

#[METHOD #1] 
#-----------
#The os.system Function
#Allows for the immedate execution of a shell command from within Python.
"""
The echo commmand prints to STDOUT, os.system() also displays the output of the STDOUT stream.
The os.system Function does the following:
  - executes a command
 - prints any output of the command to console
 - returns the exit code of the command
"""
import os

os.system("echo Hello from Python!")                                    #Hello from Python!

#While not visible in the console, the os.system() command returns the exit code of the shell command.
# - An exit code of 0 means that no error were encountered.
import os

exit_code = os.system("cd ~")

print("`cd ~` ran with exit code %d" % exit_code)                        #`cd ~` ran with exit code 0

exit_code = os.system("cd doesnotexist")

print("`cd doesnotexist` ran with exit code", exit_code)              #`cd doesnotexist` ran with exit code 512

#[METHOD #2] 
#-----------
#The subprocess Module
#This is Python's recommended way of executing shell commands. 
"""
The subprocess module provides for the ability to:
 - suppress the output of shell commands
 - chain inputs and outputs of various commands together

Note: Arguments should be separated based on space:
- ls -alh               -->     ["ls", "-alh"]
- ls -a -l -h           -->     ["ls", "-a", "-l", "-h"]
- echo Hello World      -->     ["echo", "Hello", "World"]
- echo "Hello World"    -->     ["echo", "Hello World"]
- echo hello\ world     -->     ["echo", "Hello World"]

"""
import subprocess

list_files = subprocess.run(["ls", "-l"])

print("The exit code was: %d" % list_files.returncode)                  #total 172
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  9047 Oct 26 12:05 JSON.py
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  1314 Oct 26 17:03 PIP.py   
                                                                        #...
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal   296 Oct 23 16:35 user_input.py
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  2241 Oct 22 08:11 variables.py
                                                                        #The exit code was: 0

#Piping STDOUT to /dev/null
import subprocess

list_files = subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)

print("The exit code was: %d" % list_files.returncode)                  #The exit code was: 0

#Providing Input to a Command
import subprocess

useless_cat_call = subprocess.run(["cat"], stdout=subprocess.PIPE, text=True, input="Hello from the other side.")

print(useless_cat_call.stdout)                                          #Hello from the other side.

#Where:
# - stdout=subprocess.PIPE                  Tells Python to redirect the output of the command to an object so it can be manually read later.
# - text=True                               Returns STDOUT and STDERR as strings (default return type is bytes).
# - input="Hello form the other side."      Tells Python to add the string as input to he cat command.

#Raising an Exception
#We can also reaise an exception without manually checking the return value.
import subprocess

#failed_command = subprocess.run(["false"], check=True)      #using check=True allows for the raising of exceptions

#print("The exit code was: %d" % failed_command.returncode)             #Traceback (most recent call last):
                                                                        #  File "./shell.py", line 80, in <module>
                                                                        #    failed_command = subprocess.run(["false"], check=True)
                                                                        #  File "/usr/lib/python3.8/subprocess.py", line 512, in run
                                                                        #    raise CalledProcessError(retcode, process.args,
                                                                        #subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.

#[METHOD #3] 
#-----------
#Running a Command Popen
#The subprocess.Popen class exposes more options to the developer.
"""
By default, the subprocess.Peopen does not stop processing of a Python program if its command has not finished executing.
"""

#The wait() Method 
#Temporarily halts the program from processing more code intil the list_dir command has completed.
import subprocess

list_dir = subprocess.Popen(["ls", "-l"])

list_dir.wait()                                                         #total 172
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  9047 Oct 26 12:05 JSON.py
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  1314 Oct 26 17:03 PIP.py   
                                                                        #...
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal   296 Oct 23 16:35 user_input.py
                                                                        #-rwxrwxrwx 1 dgrewal dgrewal  2241 Oct 22 08:11 variables.py

#The poll() Method
#Returns the exit code if a command has finished running or None it it is still running.
import subprocess

list_dir = subprocess.Popen(["ls", "-l"])

exit_code = list_dir.poll()

print(exit_code)                                                        #None

#The communicate() Method
#Manages input and output with subprocess.Popen
#Takes an input argument (STDIN) that is used to pass input to the shell command and returns STDOUT and STDERR.
import subprocess

useless_cat_call = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, errors = useless_cat_call.communicate(input="Hello from the other side!")

useless_cat_call.wait()

print(output)                                                           #Hello from the other side!
print(errors)                                                           #



#Which One Should be Used?
"""
If you need to run a few simple commands and don't mind if their output goes to the console:   os.system()
If you want to manage the input and outout of a shell command:                                 subprocess.run()
If you want to run a command and continue doing other work while it is being executed:         subprocess.Popen()

                                        os.system()    subprocess.run()    subprocess.Popen()
                                        -------------  ------------------  ------------------
Requires parsed arguments                              X                   X
Waits for the command                   X              X
Communicates with STDIN and STDOUT                     X                   X
Returns                                 return value   object              object
"""