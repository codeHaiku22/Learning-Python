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
#As a Python developer, you can choose to throw an exception if a condition occurs.
#To throw/raise an exception, use the raise keyword.
x = -1

if x < 0:
   #raise Exception("Sorry, no numbers below zero.")    #Exception: Sorry, no numbers below zero.

#You can define what kind of error to raise and the text to print to the user.
    x = "hello"

if not type(x) is int:
   #raise TypeError("Only intergers are allowed.")      #TypeError: Only integers are allowed.
    pass

#The assert Statement
#The assertion is a sanity-check that can be turgned off when testing is complete.
#It can be thought of an a raise-if-not statement; whereas when the result is false, the exception is raised.
#Assertions are often made at: 
# - the beginning of a function to check for valid input
# - after a function call to check for valid output
def KelvintoFahrenheit(temperature):
    assert (temperature >= 0), "Colder than absolute zero - 0K!"
    return ((temperature - 273) * 1.8) + 32

print(KelvintoFahrenheit(273))                          #32.0
print(int(KelvintoFahrenheit(505.78)))                  #451
#print(KelvintoFahrenheit(-5))                          #AssertionError: Colder than absolute zero - 0K!


#Identify an Exception

#METHOD #1: Using the Exception keyword and the exception by name
try:
    a = 5 / 0
except Exception as e:
    print(e)                                            #division by zero

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)                                            #unsupported operand type(s) for +: 'float' and 'str'
else:
    print("Everything is fine.")
finally:
    print("Cleaning up.")                               #Cleaning up.

#METHOD #2" Using the sys.exec_info() function
#The sys.exec_info() function returns the details of the exception.  
# - This allows us to identify the error and refer to it by name in the except clause.
import sys

try:
    f = open('/home/andrew_mallet/file11')
except:
    print(sys.exc_info())                               #Full error: (<class 'FileNotFoundError'>, FileNotFoundError(2, 'No such file or directory'), <traceback object at 0x7f54b772e900>)
    print(sys.exc_info() [0])                           #Error Name: <class 'FileNotFoundError'>

try:
    f = open('/home/andrew_mallet/file11')    
except FileNotFoundError:
    print("Sorry, this file could not be found.")    

#Defining a Custom Exception
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooLowError('value is too low', x)

#test_value(150)                                        #__main__.ValueTooHighError: value is too high

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)                                            #value is too high
except ValueTooLowError as e:
    print(e.message, e.value)                           #value is too low 1