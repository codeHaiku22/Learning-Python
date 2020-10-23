#!/usr/bin/python3

#Python Loops
"""
Python has 2 primitve loops:
  - while loops
  - for loops
"""

#Python While Loops
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1

while i < 5:
    print(i)                                    #1
    i += 1                                      #2
                                                #3
                                                #4

#The break Statement
#Stops the loop even if the while condition is true.
i = 1

while i < 5:
    print(i)                                    #1
    if i == 3:                                  #2    
        break                                   #3
    i += 1

#The continue Statement
#Stops the current iteration of the loop and continues to the next iteration.
i = 1

while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)                                    #3
                                                #4
                                                #5

#The else Statement
#Specifies a block of code to be executed when the loop is finished (the while condition is no longer true)
i = 1

while i < 6:
    print(i)                                    #1
    i += 1                                      #2
else:                                           #3
    print("i is no longer less than 6.")        #4
                                                #5
                                                #i is no longer less than 6.

#Python For Loops
#A for loop is used for iterating over a sequence (list, tuple, dictionary, set, string)
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)                                    #apple
                                                #banana
                                                #cherry

for x in "banana":                              
    print(x)                                    #b            
                                                #a
                                                #n
                                                #a
                                                #n
                                                #a

#The break Statement
#Stops the loop before completion.
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)                                    #apple
    if x == "banana":                           #banana
        break

#The continue Statement
#Stops the current iteration of the loop and continues to the next iteration.
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)                                    #apple
                                                #cherry

#The range() Function
#Loop through a set of code a specified number of times.
#Returns a sequence of numbers starting from 0 (by default), increments by 1 (by default), and ends at specified number.
for x in range(6):
    print(x)                                    #0
                                                #1
                                                #2
                                                #3
                                                #4
                                                #5
for x in range(2, 6):
    print(x)                                    #2
                                                #3
                                                #4
                                                #5

for x in range(10, 30, 3):                      
    print(x)                                    #10
                                                #13
                                                #16
                                                #19
                                                #22
                                                #25
                                                #28

#Else in For Loop
#Specifies a block of code to be executed when the loop is finished
for x in range(4):
    print(x)                                    #0
                                                #1
                                                #2
                                                #3
else:
    print("Finally finished!")                  #Finally finished!

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]                                             

for x in adj:
    for y in fruits:
        print(x, y)                             #red apple
                                                #red banana
                                                #red cherry
                                                #big apple
                                                #big banana
                                                #big cherry
                                                #tasty apple
                                                #tasty banana
                                                #tasty cherry
#The pass Statement
#for loops cannot be empty, but if you for some reason hav ea for loop with no content, ut in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass