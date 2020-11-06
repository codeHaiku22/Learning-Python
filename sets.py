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

#Set Methods
"""
Method                          Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()          Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""

#Set
#A set is a collection which is unordered and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)                              #{'cherry', 'banana', 'apple'}

#Access Items
#You cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)                                #cherry
                                            #apple
                                            #banana

#Change Item Value
#Once a set is created, you cannot change its items, but you can add new items.

#Add items

#add()
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.add("papaya")
print(thisset)                              #{'papaya', 'cherry', 'kiwi', 'mango', 'orange', 'nectarine', 'banana', 'apple'}

#update()
#Add multiple items to a set using the update() method.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.update(["papaya", "strawberry", "zuchini"])
print(thisset)                              #{'nectarine', 'mango', 'orange', 'zuchini', 'papaya', 'banana', 'kiwi', 'cherry', 'strawberry', 'apple'}

#Get the Length of a Set

#The len() method can be used to dtermine how many items are in a set.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
print(len(thisset))                         #7

#Remove Items

#remove()
#Removes a specified item 
#If the item does not exist, it will raise an error.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.remove("banana")
print(thisset)                              #{'cherry', 'kiwi', 'mango', 'apple', 'orange', 'nectarine'}

#discard
#If the item does not exist, it will NOT raise an error.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.discard("banana")
print(thisset)                              #{'cherry', 'kiwi', 'mango', 'apple', 'orange', 'nectarine'}}

#pop()
#Removes the last item of the set
#Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.pop()
print(thisset)                              #{'apple', 'nectarine', 'kiwi', 'mango', 'cherry', 'orange'}

#clear()
#Empties the set
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
thisset.clear()
print(thisset)                              #set()

#del()
#Deletes the set completely.
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
del thisset
#print(thisset)                             #NameError: name 'thisset' is not defined

#Copy a set
#You cannot copy a set simply by typing set2 = set1, because: set2 will only be a reference to set1, and changes made in set1 will automatically also be made in set2.

#copy()
thisset = {"apple", "banana", "cherry", "kiwi", "mango", "nectarine", "orange"}
newset = thisset.copy()
print(newset)                               #{'apple', 'banana', 'cherry', 'kiwi', 'mango', 'nectarine', 'orange'}

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
#Removes the items in this set that are also included in another specified set
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
print(isSuperset)                           #False

#symmetric_difference()
#Return a set that contains all items from both sets, except items that are present in both set (everything except the matching items)
ubuntuSet = {"Pop!_os", "KDE Neon", "Xubuntu", "Kubuntu", "Lubuntu", "Ubuntu Mate", "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin", "Zorin", "elementaryOS", "Ubuntu"}
debianSet = {"Deepin", "Ubuntu", "Debian", "MX Linux", "Kali Linux", "PureOS", "Raspian", "Linux Mint"}

newSet = ubuntuSet.symmetric_difference(debianSet)
print(newSet)                               #{'Ubuntu Kylin', 'Pop!_os', 'Linux Mint', 'Lubuntu', 'PureOS', 'Deepin', 'Xubuntu', 'Debian', 'Kubuntu', 'Zorin', 'Raspian', 'Ubuntu Mate', 'KDE Neon', 'Kali Linux', 'Ubuntu Budgie', 'elementaryOS', 'Ubuntu Studio', 'MX Linux'}

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

#Frozen Sets
#A frozen set is one that, after being created, cannot be changed.
frznSet = frozenset([1, 2, 3 ,4])
print(frznSet)                            #frozenset({1, 2, 3, 4})