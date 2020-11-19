#!/usr/bin/python

#Python Decorators
"""
A decorator takes a function, extends it and returns (a function can return a function).
Decorators add functionality to an existing function (meta-programming).
A function can take a function as an argument (the function to be decorated) and return the same function with or without extension.
Extending functionality is very useful.
"""

#Function Decorators

#In Python everything is an object, including functions.
def hello():
    print("Hello")

message = hello

message()                                       #Hello

#A decorator takes a function, extends it, and returns.
#A function can return a function!
def hello(func):
    def inner():
        print("Hello ")
        func()    #name()
    return inner

def name():
    print("Alice")

obj = hello(name) #hello decorates name
obj()                                           #Hello
                                                #Alice

#Functions can be extended by wrapping them
def who():
    print("Alice")

def display(func):
    def inner():
        print("The current user is: ", end="")
        func()
    return inner

if __name__ == "__main__":
    myobj = display(who) #display decorates who
    myobj()                                     #The current user is: Alice

#Decorators are common and can be simplified with the @ symbol.
#The call:
#  @hello
#  def name()
#Is a simpler way of writing:
#  obj = hello(name)
def hello(func):
    def inner():
        print("Hello ")
        func()    #name()
    return inner

@hello
def name():
    print("Alice")

if __name__ == "__main__":
    name()                                      #Hello
                                                #Alice

#Arguments or parameters can be used with decorators.
def pretty_sumab(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a,b)
    return inner

@pretty_sumab
def sumab(a,b):
    summed = a + b
    print(summed)    
    
if __name__ == "__main__":
    sumab(5,3)                                  #5 + 3 is 8

#A "real-world" example of decorators
import time

def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time() - t) + " seconds to run.")
        return res
    return wrapper

@measure_time
def myfunction(n):
    time.sleep(n)

if __name__ == "__main__":
    myfunction(2)                               #Function took 2.0013043880462646 seconds to run.

#Another basic example of a decorator function
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print ('End')
    return wrapper

def print_name():
    print('Alex')

print_name()                                    #Alex

#Add the decorator to the function call.
print_name = start_end_decorator(print_name)

print_name()                                    #Start
                                                #Alex
                                                #End

#Using the @ sign for adding the decorator to the function call.
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print ('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

print_name()                                    #Start
                                                #Alex
                                                #End

#Using *args and **kwargs

#If we try to pass an argument to a decorated function without 
def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print ('End')
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

#add5(10)                                       #TypeError: wrapper() takes 0 positional arguments but 1 was given

#To pass in a variable to a a function with a decorator, the wrapper function will need to be changed to take in an input parameter
def start_end_decorator(func):
    def wrapper(x):       #input parameter added
        print('Start')
        result = func(x)  #result set to output which also included input parameter
        print ('End')
        return result     #result is returned
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10) 
print(result)                                   #Start
                                                #End
                                                #15

#To pass in an unknown number of argument, the wrapper will have to be modified to take in *args and **kwargs
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print ('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10) 
print(result)                                   #Start
                                                #End
                                                #15

#Obtaining information about a function.

#The code below will not output much information.
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print ('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))                               #Help on function wrapper in module __main__:
                                                #wrapper(*args, **kwargs)
                                                #(END)
print(add5.__name__)                            #None
                                                #wrapper

#Using the functools module, we can get more information.
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print ('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))                               #Help on function add5 in module __main__:
                                                #add5(x)
                                                #(END)
print(add5.__name__)                            #None
                                                #add5                                                

#Another example
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
        print(f'Hello, {name}!')

greet('Alex')                                   #Hello, Alex!
                                                #Hello, Alex!
                                                #Hello, Alex!

#Using nested decorators
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello, {name} !'
    print(greeting)
    return greeting

say_hello('Alex')                               #Calling say_hello('Alex')
                                                #Start
                                                #Hello, Alex!
                                                #End
                                                #'say_hello' returned 'Hello, Alex!'

#Class Decorators

#Create a class decorator and perform a test to ensure that it works.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        print('Hi there')

cc = CountCalls(None)
cc()                                            #Hi there

@CountCalls
def say_hello():
    print('Hello!')

#Now let's implement the actual class decorator and demonstrate the cumulative/incrementing behavior.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times.')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello!')    

say_hello()                                     #This is executed 1 times.
                                                #Hello
say_hello()                                     #This is executed 2 times.
                                                #Hello                                                