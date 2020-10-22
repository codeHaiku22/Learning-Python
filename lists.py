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

#List Methods
"""
Method      Description
append()    Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()   Reverses the order of the list
sort()	    Sorts the list
"""

#List
#A list is a collection which is ordered and changeable.
thislist = ["apple", "banana", "cherry"]
print(thislist)                             #['apple', 'banana', 'cherry']

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])                          #banana

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])                         #cherry

#Range of Indexes
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[2:5])                        #['cherry', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[:4])                         #['apple', 'banana', 'cherry', 'kiwi']

thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[2:])                         #['cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#Range of Negative Indexes
#Returns the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[-4:-1])                       #['kiwi', 'mango', 'nectarine']

#Returns the items from index -5 (included) to index -2 (excluded)
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[-5:-2])                       #['cherry', 'kiwi', 'mango']

#Returns the items from index -5 (included) to end
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[-5:])                       #['cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#Returns the items from index 0 (included) to -2(excluded)
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(thislist[:-2])                       #['apple', 'banana', 'cherry', 'kiwi', 'mango']

#Change Item Value
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist[1] = "blackberry"
print(thislist)                            #['apple', 'blackberry', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#Loop Through a List
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
for x in thislist:
    print(x)                               #apple
                                           #banana
                                           #cherry
                                           #kiwi
                                           #mango
                                           #nectarine
                                           #orange

#Check if Item Exists
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
if "apple" in thislist:
    print("Yes, 'apple' is in the list.")  #Yes, 'apple' is in the list.

#List Length
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
print(len(thislist))                       #7

#Add items

#append()
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.append("papaya")
print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange', 'papaya']

#insert()
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.insert(4, "lime")
print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'lime', 'mango', 'nectarine', 'orange']

#Remove Items

#remove()
#Removes a specified item
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.remove("banana")
print(thislist)                            #['apple', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#pop()
#Removes a specified index (or last item if index is not specified)
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.pop(3)
print(thislist)                            #['apple', 'banana', 'cherry', 'mango', 'nectarine', 'orange']

thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.pop()
print(thislist)                            #["apple", "banana", "cherry", "kiwi", "mango", "nectarine"]

#del
#Removes a specified index (or entire list if index is not specified)
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
del thislist[0]
print(thislist)                            #['banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
del thislist
#print(thislist)                            #NameError: name 'thislist' is not defined

#clear()
#Empties the list
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.clear()
print(thislist)                            #[]

#Ordering Items

#sort()
#Sort a list
thislist = ["apple", "cherry", "banana", "kiwi", "mango", "nectarine", "orange"]
thislist.sort()
print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#reverse()
#Reverses the order of the list
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thislist.reverse()
print(thislist)                            #['orange', 'nectarine', 'mango', 'kiwi', 'cherry', 'banana', 'apple']

#Locating Items

#index
#Returns the index of the first element with the specified value
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
i = thislist.index("kiwi")
print(i)                                   #3

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

#copy()
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
newlist = thislist.copy()
print(newlist)                             #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#list()
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
newlist = list(thislist)
print(newlist)                             #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']

#Join Two Lists

#Using +
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thatlist = ["papaya", "strawberry", "zuchini"]
mylist = thislist + thatlist                
print(mylist)                              #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange', 'papaya', 'strawberry', 'zuchini']

#Loop
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thatlist = ["papaya", "strawberry", "zuchini"]

for x in thatlist:
    thislist.append(x)

print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange', 'papaya', 'strawberry', 'zuchini']

#extend()
#Add the elements of a list (or any iterable) to the end of the current list
thislist = ["apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"]
thatlist = ["papaya", "strawberry", "zuchini"]
thislist.extend(thatlist)
print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange', 'papaya', 'strawberry', 'zuchini']

#The list() Constructor
#It is also possible to use the list() constructor to make a new list
thislist = list(("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"))
print(thislist)                            #['apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange']