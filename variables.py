#!/usr/bin/python3

#Creating Variables
x = 5
y = "John"
print(x)
print(y)

z = 4
z = "Sally"
print(z)

#Both a and b are the same with double quotes and single quotes
a = "John"  
b = 'John'
print(a,b)

#Variable Names
"""
Rules for Python Variables
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, _)
- Variable names are case-sensitive
"""
#Assign Value to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Output Variables
#To combine both text and a variable, use the + character for concatenation.
x = "awesome"
print("Python is " + x + "!")

#You can also use the + character to concatenate a variable to another variable.
x = "Python is "
y = "awesome"
z = x + y + "!"
print(z)

#For numbers, the + character works as a mathematical operator: addition.
x = 5
y = 10
print(x + y)

#Global Variables
#Wariables that are created outside of a function are known as global variables.
#They can be used by everyone, both inside and outside of functions.
x = "awesome"

def myfunc():
    print("Python is " + x + "!")

myfunc()

#If you create a variable with the same name inside of a function, the variable will be local and can only be used inside the function.
#The global variable with the same name will remain as it was, global, and retain its original value.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x + "!")

myfunc()

print("Python is " + x + "!")

#The global Keyword
#Normally, when you create a variable inside of a function, that variable is local, and can only be used inside that function.
#To create a global variable inside of a function, you can use the flobal keyword.
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x + "!")

#Also, use the global keyword if yu want to change a global variable inside of a function.
x = "awesome"

def myfun():
    global x 
    x = "fantastic"

myfunc()

print("Python is " + x + "!")