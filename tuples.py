#!/usr/bin/python3

#Python Collection Arrays
"""
There are 4 collection data types in the Python programming language.

Type         Ordered  Indexed  Changeable  Duplicates
-----------  -------  -------  ----------  ----------                 
List         X        X        X           X
Tuple        X        X                    X
Set                            X   
Dictionary            X        X
"""

#Tuple Methods
"""
Method      Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
"""

#Tuple
#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)                             #('apple', 'banana', 'cherry')

#Access Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])                          #banana

#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])                         #cherry

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[2:5])                        #('cherry', 'kiwi', 'mango')

thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[:4])                         #('apple', 'banana', 'cherry', 'kiwi')

thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[2:])                         #('cherry', 'kiwi', 'mango', 'nectarine', 'orange')

#Range of Negative Indexes
#Returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[-4:-1])                       #('kiwi', 'mango', 'nectarine')

#Returns the items from index -5 (included) to index -2 (excluded)
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[-5:-2])                       #('cherry', 'kiwi', 'mango')

#Returns the items from index -5 (included) to end
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[-5:])                       #('cherry', 'kiwi', 'mango', 'nectarine', 'orange')

#Returns the items from index 0 (included) to -2(excluded)
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(thistuple[:-2])                       #('apple', 'banana', 'cherry', 'kiwi', 'mango')

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
thislist = list(thistuple)
thislist[1] = "blackberry"
thistuple = tuple(thislist)

print(thistuple)                            #('apple', 'blackberry', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange')

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
for x in thistuple:
    print(x)                               #apple
                                           #banana
                                           #cherry
                                           #kiwi
                                           #mango
                                           #nectarine
                                           #orange

#Check if Item Exists
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple.")  #Yes, 'apple' is in the tuple.

#Tuple Length
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
print(len(thistuple))                      #7

#Add items
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

#Create Tuple with One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(thistuple)                           #('apple',)

#Remove Items
#Once a tuple is created, you cannot remove items from it. Tuples are unchangeable.

#del
#Delete the tuple completely
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
del thistuple
#print(thistuple)                           #NameError: name 'thistuple' is not defined

#Join Two Tuples

#Using +
thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange")
thattuple = ("papaya", "strawberry", "zuchini")
mytuple = thistuple + thattuple                
print(mytuple)                              #('apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange', 'papaya', 'strawberry', 'zuchini')

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a new tuple
thistuple = tuple(("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"))
print(thistuple)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']