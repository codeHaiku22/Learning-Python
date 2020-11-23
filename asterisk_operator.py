#!/usr/bin/python

#The asterisk operator has many different use cases.

#USE CASE #1: Multiply Values
x = 2 * 3 * 5
print(x)                                                    #30

#USE CASE #2: Calculate the Exponent of a Value
x = (2 ** 3)
print(x)                                                    #8

#USE CASE #3: Create Container Data Types/Repition
lst = [999999] * 5
print(lst)                                                  #[999999, 999999, 999999, 999999, 999999]

lst = [0, 1] * 5
print(lst)                                                  #[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

tple = (5, 7) * 3
print(tple)                                                 #(5, 7, 5, 7, 5, 7)

string = "XO" * 7
print(string)                                               #XOXOXOXOXOXOXO

#USE CASE #4: Create a Function with an Arbitrary Number of Positional Arguments (*args)
def average(*args):
    return sum(args) / len(args)

avg = average(999.0, 966.3, 988.2, 1344.5)    
print(avg)                                                  #1074.5

#USE CASE #5: Create a Function with an Aribitrary Number of Keyword Arguments (**kwargs)
def knows(**kwargs):
    for key in kwargs:
        print(key + " knows " + kwargs[key])

print(knows(Alice="Bob", Bob="Ann", Ann="Alice"))           #Alice knows Bob
                                                            #Bob knows Ann
                                                            #Ann knows Alice
                                                            #None

#USE CASE #6: Unpack a Dictionary
trucksDict = {"Toyota" : "Tundra", "Ford" : "F-150", "Chevrolet" : "Silverado", "Ram" : "1500"}        
print(trucksDict)                                           #{'Toyota': 'Tundra', 'Ford': 'F-150', 'Chevrolet': 'Silverado', 'Ram': '1500'}
print(*trucksDict)                                          #Toyota Ford Chevrolet Ram

#With a function
def makeModels(**kwargs):
    for key in kwargs:
        print(key + " " + kwargs[key])

trucksDict = {"Toyota" : "Tundra", "Ford" : "F-150", "Chevrolet" : "Silverado", "Ram" : "1500"}        

makeModels(**trucksDict)                                    #Toyota Tundra
                                                            #Ford F-150
                                                            #Chevrolet Silverado
                                                            #Ram 1500

#USE CASE #7: Unpack a List, Tuple, Set
#List
students = ["Cata", "Brian", "Myu", "Joey"]                                                            
print(students)                                             #['Cata', 'Brian', 'Myu', 'Joey']
print(*students)                                            #Cata Brian Myu Joey

#List - With a function
def say_hello(*args):
    for a in args:
        print("Hello, " + a + "!")

students = ["Cata", "Brian", "Myu", "Joey"] 
say_hello(*students)                                        #Hello, Cata!
                                                            #Hello, Brian!
                                                            #Hello, Myu!
                                                            #Hello, Joey!

#List - Using positional notation
numbers = [1, 2, 3, 4, 5, 6]                                                            

*beginning, ending = numbers
print(beginning)                                            #[1, 2, 3, 4, 5]
print(ending)                                               #6

beginning, *ending = numbers
print(beginning)                                            #1
print(ending)                                               #[2, 3, 4, 5, 6]

#Tuples
fruits = ("apple", "banana", "cherry", "durian")                                                            
print(fruits)                                               #('apple', 'banana', 'cherry', 'durian')
print(*fruits)                                              #apple banana cherry durian

#Tuple - With a function
def say_colorful(*args):
    for a in args:
        print("Colorful " + a + "!")

fruits = ("apple", "banana", "cherry", "durian")
say_colorful(*fruits)                                       #Colorful apple!
                                                            #Colorful banana!
                                                            #Colorful cherry!
                                                            #Colorful durian!

#Tuple - Using positional notation
numbers = (1, 2, 3, 4, 5, 6)                                                            

*beginning, ending = numbers
print(beginning)                                            #[1, 2, 3, 4, 5]
print(ending)                                               #6

beginning, *ending = numbers
print(beginning)                                            #1
print(ending)                                               #[2, 3, 4, 5, 6]

#Sets                                                            
tools = {"screwdriver", "hammer", "wrench", "drill"}
print(tools)                                                #{'hammer', 'drill', 'screwdriver', 'wrench'}
print(*tools)                                               #hammer drill screwdriver wrench  

#Set - With a function
def say_handy(*args):
    for a in args:
        print("Handy " + a + "!")

tools = {"screwdriver", "hammer", "wrench", "drill"}
say_handy(*tools)                                           #Handy hammer!!
                                                            #Handy drill!!
                                                            #Handy screwdriver!
                                                            #Handy wrench!

#Set - Using positional notation
numbers = {1, 2, 3, 4, 5, 6}                                                            

*beginning, ending = numbers
print(beginning)                                            #[1, 2, 3, 4, 5]
print(ending)                                               #6

beginning, *ending = numbers
print(beginning)                                            #1
print(ending)                                               #[2, 3, 4, 5, 6]                                                            

#USE CASE #8: Merge Lists, Tuples, Sets        
#Lists                                                    
students1 = ["Cata", "Brian", "Myu", "Joey"]
students2 = ["Jim", "Leanne", "Suzy", "Francis"]                                                            

students = [*students1, *students2]                         
print(students)                                             #['Cata', 'Brian', 'Myu', 'Joey', 'Jim', 'Leanne', 'Suzy', 'Francis']

#Tuples
fruits1 = ("apple", "banana", "cherry", "durian")
fruits2 = ("jackfruit", "kiwi", "lemon", "mandarin")

fruits = (*fruits1, *fruits2)                         
print(fruits)                                               #('apple', 'banana', 'cherry', 'durian', 'jackfruit', 'kiwi', 'lemon', 'mandarin') 

#Sets
tools1 = {"screwdriver", "hammer", "wrench", "drill"}
tools2 = {"saw", "pliers", "ruler", "vice"}

tools = {*tools1, *tools2}                         
print(tools)                                                #{'ruler', 'hammer', 'drill', 'pliers', 'saw', 'screwdriver', 'wrench', 'vice'}       

#Mixed
students1 = ["Cata", "Brian", "Myu", "Joey"]
fruits1 = ("apple", "banana", "cherry", "durian")
tools1 = {"screwdriver", "hammer", "wrench", "drill"}

mixed = [*students1, *fruits1, *tools1]
print(mixed)                                                #['Cata', 'Brian', 'Myu', 'Joey', 'apple', 'banana', 'cherry', 'durian', 'wrench', 'hammer', 'drill', 'screwdriver']

mixed = (*students1, *fruits1, *tools1)
print(mixed)                                                #('Cata', 'Brian', 'Myu', 'Joey', 'apple', 'banana', 'cherry', 'durian', 'hammer', 'screwdriver', 'wrench', 'drill')

mixed = {*students1, *fruits1, *tools1}
print(mixed)                                                #{'drill', 'Brian', 'Myu', 'durian', 'cherry', 'Cata', 'apple', 'hammer', 'wrench', 'Joey', 'screwdriver', 'banana'}

#USE CASE #9: Merge Dictionaries
trucksDict1 = {"Toyota" : "Tundra", "Ford" : "F-150", "Chevrolet" : "Silverado", "Ram" : "1500"} 
trucksDict2 = {"Honda" : "Ridgeline", "Nissan" : "Titan", "GMC" : "Sierra"}

trucksDict = {**trucksDict1, **trucksDict2}
print(trucksDict)                                           #{'Toyota': 'Tundra', 'Ford': 'F-150', 'Chevrolet': 'Silverado', 'Ram': '1500', 
                                                            # 'Honda': 'Ridgeline', 'Nissan': 'Titan', 'GMC': 'Sierra'}

#USE CASE #10: Regular Expressions (RegEx) 
#The zero-or-more asterisk matches an arbitrary number of occurrences (including zero occurrences) of the immediately preceding regex.
import re

text = 'finxter for fast and fun python learning'

result = re.findall('f.* ', text)
print(result)                                               #['finxter for fast and fun python ']

result = re.findall('f.*? ', text)
print(result)                                               #['finxter ', 'for ', 'fast ', 'fun ']

result = re.findall('f[a-z]*', text)
print(result)                                               #['finxter', 'for', 'fast', 'fun']