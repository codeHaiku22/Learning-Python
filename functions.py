#!/usr/bin/python3

#Creating a Function
def my_function():
    print("Hello from a function.")                         

#Calling a function
my_function()                                                                       #Hello from a function.

#Arguments (args)
def hello_function(fname):
    print("Hello, "+ fname + "!")

hello_function("Deep")                                                              #Hello, Deep!

#Arbitrary Arguments (*args)
#If you don't know how many arguments will be passed into your function, add an asterisk (*) before the parameter name in the function definition.
#This lets the function receive a tuple of arguements.
def youngestkid_function(*kids):
    print("The youngest child is " + kids[2] + ".")

youngestkid_function("Jazlyn", "Ronin", "Kaizen")                                   #The youngest child is Kaizen.

#Keyword Arguments (kwargs)
#You can also send arguments with the key = value syntax.
#This way the order of arguments does not matter.
def oldestkid_function(child1, child2, child3):
    print("The oldest child is " + child1 + ".")

oldestkid_function(child1 = "Jazlyn", child2 = "Ronin", child3 = "Kaizen")          #The oldest child is Jazlyn.

#Arbitrary Keyword Arguments (**kwargs)
#If you do not know how many keyword arguments that will be passed into your function, add 2 asterisks (**) befor ethe parameter name in the function definition.
#This letsthe function receive a dictionary of arguments.
def lastname_function(**kid):
    print("His last name is " + kid["lname"] + ".")

lastname_function(fname = "Ronin", lname = "Grewal")                                #His last name is Grewal.

#Default Parameter Value
def country_function(country = "United States of America"):
    print("I am from " + country + ".")

country_function("India")                                                           #I am from India.
country_function()                                                                  #I am from United States of America.

#Passing a List as an Argument
#You can send any data types of arguments to a function and it will be treated as the same data type inside the function.
def food_function(food):
    for x in food:
        print(x)

food = ["pizza", "burrito", "salad"]

food_function(food)                                                                 #pizza
                                                                                    #burrito
                                                                                    #salad

#Return Values
#To return values from a function use the "return" statement.
def area_fuction(length, width):
    area = length * width
    return area

print(area_fuction(3, 5))                                                           #15

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def empty_function():
    pass

#Recursion
#In this example, tri_recursion() is a function calls itself (recurses).
#The k variable is the data which is decremented by -1 upon each recursion.
#The recursion ends with the condition is not greater than 0 (equal to 0).
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results")    
tri_recursion(6)                                                                    #Recursion Example Results
                                                                                    #1
                                                                                    #3
                                                                                    #6
                                                                                    #10
                                                                                    #15
                                                                                    #21

#Lambda

#A lambda function is a small, anonymous function.
# lamba <arguments> : <expression>
x = lambda a: a + 10
print(x(5))                                                                         #15

#It an take any number if arguments, but can only have 1 expression.
x = lambda a, b : a * b
print(x(5, 6))                                                                      #30

x = lambda a, b, c : a + b + c                                                      
print(x(5, 10, 15))                                                                 #30

#Why Use Lambda Functions?
#The power of lambda functions is best shown whn you use them as an anonymous function inside another function.

#Let's start with a function definition that takes 1 argument and then multiplies that argument by an unknown number.
def myfunc(n):
    return lambda a : a * n

#Use that function definition to make a function that always doubles the number you send in.
mydoubler = myfunc(2)
print(mydoubler(11))                                                                #22

mytripler = myfunc(3)
print(mytripler(11))                                                                #33

#Use a lambda function within a definition
#Without lambda, sort by x-coordinate
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points)       

print(points)                                                                       #[(1, 2), (15, 1), (5, -1), (10, 4)]
print(points_sorted)                                                                #[(1, 2), (5, -1), (10, 4), (15, 1)]

#Without lambda, sort by y-coordinate
points = [(1, 2), (15, 1), (5, -1), (10, 4)]

def sort_by_y(x):
    return x[1]

points_sorted = sorted(points, key=sort_by_y)

print(points)                                                                       #[(1, 2), (15, 1), (5, -1), (10, 4)]
print(points_sorted)                                                                #[(5, -1), (15, 1), (1, 2), (10, 4)]

#With lambda, sort by y-coordinate
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points, key=lambda x: x[1])

print(points)                                                                       #[(1, 2), (15, 1), (5, -1), (10, 4)]
print(points_sorted)                                                                #[(5, -1), (15, 1), (1, 2), (10, 4)]

#Using the map function with a lambda function
#Without lambda - using list comprehension
a = [1, 2, 3, 4, 5]
b = [x*2 for x in a]
print(b)                                                                            #[2, 4, 6, 8, 10]

#With lambda
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)                               
print(b)                                                                            #<map object at 0x7f668adced90>
print(list(b))                                                                      #[2, 4, 6, 8, 10]   

#Without lambda - using list comprehension
a = [1, 2, 3, 4, 5, 6]
b = [x for x in a if x%2==0]
print(b)                                                                            #[2, 4, 6]

#With lambda
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b))                                                                      #[2, 4, 6]

#Using the reduce function with a lambda function
#Without lambda using a loop
a = [1, 2, 3, 4, 5, 6]
fac = 1

for i in a:
    fac *= i

print(fac)                                                                          #720

#Without lambda using a function
a = [1, 2, 3, 4, 5, 6]

def factorial(a):
    fac = 1
    for i in a:
        fac *= i
    return fac

print(factorial(a))                                                                 #720

#Without lambda
from functools import reduce

a = [1, 2, 3, 4, 5, 6]

def my_prod(a, b):
    return a * b

fac = reduce(my_prod, a)
print(fac)                                                                          #720

#With lambda
from functools import reduce

a = [1, 2, 3, 4, 5, 6]
fac = reduce(lambda x,y: x*y, a)
print(fac)                                                                          #720