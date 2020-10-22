#!/usr/bin/python3

#Boolean Values
#You can evaluate any expression in Python, and get one of two answers, True or False.
print(10 > 9)       #True
print(10 == 9)      #False
print(10 < 9)       #False

#if Statement
a = 200
b = 33

if b > a:
  print("b is greater than a")          #b is not greater than a
else:
  print("b is not greater than a") 

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value and returns True or False.

#Evaluate a string and a number
print(bool("Hello"))        #True
print(bool(15))             #True

#Evaluate two variables
x = "Hello"
y = 15

print(bool(x))              #True
print(bool(y))              #True

#Most Values are True
"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
#Almost any value is evaluated to True if it has some sort of content.
bool("abc")                                 #True
bool(123)                                   #True
bool(["apple", "cherry", "banana"])         #True

#There are not many values that evaluate to False, except empty values, False, None, and 0.
bool(False)                                 #False
bool(None)                                  #False 
bool(0)                                     #False
bool("")                                    #False
bool(())                                    #False
bool([])                                    #False
bool({})                                    #False

#If you have an object that is made from a class with a __len__ function that returns 0 or False.
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))                          #False

#Functions Can Return a Boolean Value
def myFunction() :
  return True

print(myFunction())                         #True

if myFunction():
  print("YES!")                             #YES!
else:
  print("NO!") 

x = 200
print(isinstance(x, int))                   #True