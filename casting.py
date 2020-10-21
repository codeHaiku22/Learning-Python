#!/usr/bin/python3

#Specify a Variable Type
#Python is an object-oriented language and uses classes to define data types (including its primitive types).
"""
Casting is performed using constructor functions.
int()       Contructs an integer number from:
              - an integer literal 
              - a float literal (rounds down to nearest whole number)
              - a string literal (providing the string represents a whole number)
float()     Constructs a float number from: 
              - an integer literal 
              - a float literal
              - a string literal (providing the string represents a floar or an integer)
str()       Constructs a string from a wide variety of data types including:
              - strings
              - integer literals
              - float literals
"""

#Integers
x = int(1)
y = int(2.8)
z = int("3")

print(x)        #1
print(y)        #2
print(z)        #3

#Floats
w = float(1)
x = float(2.8)
y = float("3")
z = float("4.2")

print(w)        #1.0
print(x)        #2.8
print(y)        #3.0
print(z)        #4.2

#Strings
x = str("s1")
y = str(2)
z = str(3.0)

print(x)        #'s1'
print(y)        #'2'
print(z)        #'3.0'