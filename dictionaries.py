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

#Dictionary Methods
"""
Method              Description
clear()	            Removes all the elements from the dictionary
copy()	            Returns a copy of the dictionary
fromkeys()	        Returns a dictionary with the specified keys and value
get()	            Returns the value of the specified key
items()	            Returns a list containing a tuple for each key value pair
keys()	            Returns a list containing the dictionary's keys
pop()	            Removes the element with the specified key
popitem()	        Removes the last inserted key-value pair
setdefault()        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	        Updates the dictionary with the specified key-value pairs
values()	        Returns a list of all the values in the dictionary
"""

#Dictionary
#A dictionary is a collection which is unordered, changeable, and indexed.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}
print(thisdict)                              #{'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

x = thisdict["model"]
print(x)                                    #F-150

#Change Values
#You can change the value of a specific item by referring to its key name.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}
thisdict["trim"] = "STX"
print(thisdict)                             #{'brand': 'Ford', 'model': 'F-150', 'trim': 'STX'}

#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return values are the keys of the dictionary, but there are methods to return the values as well.

#Print all keys names in the dictionary
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

for x in thisdict:
    print(x)                                #brand
                                            #model
                                            #trim

thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

#You can also use the keys() method to return keys of a dictionary
for x in thisdict.keys():
    print(x)                                #brand
                                            #model
                                            #trim                                             

#Print all values in the dictionary
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

for x in thisdict:
    print(thisdict[x])                      #Ford
                                            #F-150
                                            #Raptor

#You can also use the values() method to return values of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

for x in thisdict.values():
    print(x)                                #Ford
                                            #F-150
                                            #Raptor

#You can loop through both keys and values by using the items() method
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

for x, y in thisdict.items():
    print(x, y)                             #brand Ford
                                            #model F-150
                                            #trim Raptor        

#Check if Key Exists
#To determine if a specified key is present in a dictionary, use the in keyword.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary.")

#Dicionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() function.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

print(len(thisdict))                        #3

#Add items
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

thisdict["color"] = "charcoal"
print(thisdict)                             #{'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor', 'color': 'charcoal'}

#Remove Items

#pop()
#Removes the item with the specified key name.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

thisdict.pop("model")
print(thisdict)                             #{'brand': 'Ford', 'trim': 'Raptor'}

#popitem()
#Removes the last inserted item (in versions before 3.7, a random item is removed instead).
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

thisdict.popitem()
print(thisdict)                             #{'brand': 'Ford', 'model': 'F-150'}

#del()
#Removes the item with the specified key name.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

del thisdict["model"]
print(thisdict)                             #{'brand': 'Ford', 'trim': 'Raptor'}

#Can also be used to delete the dictionary completely
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

del thisdict
#print(thisdict)                            #NameError: name 'thisdict' is not defined

#clear()
#Empties the dictionary
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

thisdict.clear()
print(thisdict)                            #{}

"""
#Copy a set
#You cannot copy a set simply by typing set2 = set1, because: set2 will only be a reference to set1, and changes made in set1 will automatically also be made in set2.

#copy()
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
newset = thisset.copy()
print(newset)                             #{'apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange'}

#Joining Two Sets

#union()
#Returns a new set containing all items from both sets
#Will EXCLUDE duplicate items.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thatset = {"papaya", "strawberry", "zuchini"}

myset = thisset.union(thatset)              
print(myset)                                #{'kiwi', 'orange', 'strawberry', 'papaya', 'mango', 'zuchini', 'cherry', 'nectarine', 'banana', 'apple'}

#update
#Inserts the items from one set into another
#Will EXCLUDE duplicate items.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thatset = {"papaya", "strawberry", "zuchini"}

thisset.update(thatset)              
print(thisset)                              #{'kiwi', 'orange', 'strawberry', 'papaya', 'mango', 'zuchini', 'cherry', 'nectarine', 'banana', 'apple'}

#Comparing Two Sets

#difference()
#Returns a new set containing the difference between 2 or more sets
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

newSet = ubuntuSet.difference(debianSet)    
print(newSet)                               #{'Xubuntu', 'Ubuntu Kylin', 'Pop!_os', 'KDE Neon', 'Ubuntu Mate', 'elementaryOS', 'Kubuntu', 'Lubuntu', 'Zorin', 'Ubuntu Studio', 'Ubuntu Budgie'}

#difference_update()
#Removes the items in this set that aer also included in another specified set
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

debianSet.difference_update(ubuntuSet)
print(debianSet)                            #{'Debian', 'Deepin', 'Raspian', 'PureOS', 'MX Linux', 'Kali Linux', 'Linux Mint'}

#intersection()
#Returns a new set that is the intersection of 2 other sets
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

newSet = ubuntuSet.intersection(debianSet)
print(newSet)                               #{Ubuntu}

#intersection_update()
#Removes the items iin this set that are not present in other specified sets
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

debianSet.intersection_update(ubuntuSet)
print(debianSet)                            #{Ubuntu}

#isdisjoint()
#Returns whether two sets have an intersection or not
#  - Return True if no items in first set is present in second set.
#  - Returns False if atleast one item from first set is present in second set
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

isDisjoint = ubuntuSet.isdisjoint(debianSet)
print(isDisjoint)                           #False

#issubset
#Returns whether one set contains the entirety of this set
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

isSubset = ubuntuSet.issubset(debianSet)
print(isSubset)                             #False

#issuperset
#Returns whether this set contains the entirety of another set
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

isSuperset = ubuntuSet.issuperset(debianSet)
print(isSuperset)                            #False

#symmetric_difference()
#Return a set that contains all items from both sets, except items that are present in both set (everything except the matching items)
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

newSet = ubuntuSet.symmetric_difference(debianSet)
print(newSet)                                #{'Ubuntu Kylin', 'Pop!_os', 'Linux Mint', 'Lubuntu', 'PureOS', 'Deepin', 'Xubuntu', 'Debian', 'Kubuntu', 'Zorin', 'Raspian', 'Ubuntu Mate', 'KDE Neon', 'Kali Linux', 'Ubuntu Budgie', 'elementaryOS', 'Ubuntu Studio', 'MX Linux'}

#symmetric_difference_update()
#Remove the items that are present in both sets, AND insert the items that are not present in both sets.
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

ubuntuSet.symmetric_difference_update(debianSet)
print(ubuntuSet)                            #{'Kali Linux', 'Debian', 'KDE Neon', 'PureOS', 'Raspian', 'Ubuntu Studio', 'Ubuntu Kylin', 'MX Linux', 'Pop!_os', 'Ubuntu Mate', 'Xubuntu', 'elementaryOS', 'Linux Mint', 'Zorin', 'Deepin', 'Lubuntu', 'Ubuntu Budgie', 'Kubuntu'}  

#The set() Constructor

#It is also possible to use the set() constructor to make a new set
thisset = set(("apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"))
print(thisset)                              #{'apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange'}
"""