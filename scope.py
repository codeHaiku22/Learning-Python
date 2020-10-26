#!/usr/bin/python3

#Python Scope
#A variable is only available from inside the region it is created.

#Local Scope
#A variable created inside a function belongs to the local scope of that function and can only be used inside that function.
def myfunc():
    x = 300
    print(x)

myfunc()                                        #300

#Nested Function
#The local variable can be accessed from a function within a function.
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()                                        #300
                                                #300

#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variable are available from within any scope, global and local.
x = 300

def myfunc():
    print(x)

myfunc()                                        #300

print(x)                                        #300

#Naming Variables
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables.
# - One available in the global scope - outside of the function.
# - One avaialbe in the local scope - inside of the function.
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()                                        #200

print(x)                                        #300

#Global Keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword to make the variable global in scope.
def myfunc():
    global x
    x = 300

myfunc()                                        

print(x)                                        #300

#Also, use the global keyword if you want to make a change to a global variable inside of a function.
x = 300

def myfunc():
    global x
    x = 200

myfunc()                                    

print(x)                                        #200