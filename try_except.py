#!/usr/bin/python3

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try and except blocks.

#Exception Handling
#When an exception occurs, Python will normally stop and generate an error message.
#These exceptions can be handled by the try statement.
try:
    print(x)
except:
    print("An exception has occurred.")                 #An exception has occurred.

#Many Exceptions
try:
    print(x)    
except NameError:
    print("Variable x is not defined.")                 #Variable x is not defined.
except:
    print("Something else went wrong.")

#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised.
try:
    print("Hello")                                      #Hello
except:
    print("Something went wronng.")    
else:
    print("Nothing went wrong.")                        #Nothing went wrong.

#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)    
except:
    print("Something went wrong.")                      #Something went wrong.
finally:
    print("The 'try except' is finished.")              #The 'try except' is finished.

#This can be useful to close objects and clean up resources.
try:
    f = open("demofile.txt")
    f.write("\nLorem Ipsum\n")
except:
    print("Something went wrong when writing to this file.")    
finally:
    f.close()    

#Raise an Exception
#As a Pythong developer, you can choose to throw an exception if a condition occurs.
#To throw/raise an exception, use the raise keyword.
x = -1

if x < 0:
   #raise Exception("Sorry, no numbers below zero.")    #Exception: Sorry, no numbers below zero.

#You can define what kind of error to raise and the text to print to the user.
x = "hello"

if not type(x) is int:
   #raise TypeError("Only intergers are allowed.")      #TypeError: Only intergers are allowed.