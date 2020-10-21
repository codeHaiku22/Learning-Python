#!/usr/bin/python3

#Built-in Data Types
"""
Python has the following data types built-in by default, in these categories:
Text        str
Numeric     int, float, complex
Sequence    list, tuple, range
Mapping     dic
Set         set, frozenset
Boolean     bool
Binary      bytes, bytearray, memoryview
"""

#Getting the Data Type
#You can get the data type of any object by using the type() function.
x = 5
print(type(x))                                  #<class 'int'>

#Setting the Data Type
#The data type is set when you assign a value to a variable.
x = "Hello, World!"                             #str
print(type(x))                                  #<class 'str'>

x = 20                                          #int
print(type(x))                                  #<class 'int'>

x = 20.5                                        #float
print(type(x))                                  #<class 'float'>

x = 1j                                          #complex
print(type(x))                                  #<class 'complex'>

x = ["apple", "banana", "cherry"]               #list
print(type(x))                                  #<class 'list'>

x = ("apple", "banana", "cherry")               #tuple
print(type(x))                                  #<class 'tuple'>

x = range(6)                                    #range
print(type(x))                                  #<class 'range'>

x = {"name" : "John", "age" : 36}               #dict
print(type(x))                                  #<class 'dict'>

x = {"apple", "banana", "cherry"}               #set
print(type(x))                                  #<class 'set'>

x = frozenset({"apple", "banana", "cherry"})    #frozenset
print(type(x))                                  #<class 'frozenset'>

x = True                                        #bool
print(type(x))                                  #<class 'bool'>

x = b"Hello"                                    #bytes
print(type(x))                                  #<class 'bytes'>

x = bytearray(5)                                #bytearray
print(type(x))                                  #<class 'bytearray'>

x = memoryview(bytes(5))                        #memoryview
print(type(x))                                  #<class 'memoryview'>

#Setting the Specific Data Type
x = str("Hello, World!")
print(type(x))
print(x)                                        #Hello, World!         

x = int(20)
print(type(x))
print(x)                                        #20

x = float(20.5)
print(type(x))
print(x)                                        #20.5

x = complex(1j)
print(type(x))
print(x)                                        #1j

x = list(("apple", "banana", "cherry"))
print(type(x))  
print(x)                                        #['apple', 'banana', 'cherry']

x = tuple(("apple", "banana", "cherry"))
print(type(x))
print(x)                                        #('apple', 'banana', 'cherry')

x = range(6)
print(type(x))
print(x)                                        #range(0, 6)

x = dict(name = "John", age = 36)
print(type(x))
print(x)                                        #{'name': 'John', 'age': 36}

x = set(("apple", "banana", "cherry"))
print(type(x))                                  
print(x)                                       #{'banana', 'cherry', 'apple'}         

x = frozenset(("apple", "banana", "cherry"))    
print(type(x))
print(x)                                        #frozenset({'banana', 'cherry', 'apple'})

x = bool(5)
print(type(x))
print(x)                                        #True

x = bytes(5)
print(type(x))
print(x)                                        #b'\x00\x00\x00\x00\x00'

x = bytearray(5)
print(type(x))
print(x)                                        #bytearray(b'\x00\x00\x00\x00\x00')

x = memoryview(bytes(5))
print(type(x))
print(x)                                        #<memory at 0x7f4d50aaa400>