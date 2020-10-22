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

#fromkeys()
#Returns a dictionary with the specified keys and the specified value.
k = ('key1', 'key2', 'key3')
v = 0

anotherdict = dict.fromkeys(k, v)
print(anotherdict)

#Accessing Items

#You can access the items of a dictionary by referring to its key name, inside square brackets.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

x = thisdict["model"]
print(x)                                    #F-150

#get()
#Returns the value of the items with the specified key
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

x = thisdict.get("model")
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

#You can also use the keys() method to return keys of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

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

#Return Value of Specified Key or Create New Key 
# setdefault()
# Returns the value of the item with the specified key.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

x = thisdict.setdefault("trim", "STX")
print(x)                                    #Raptor

# If the key does not exist, insert the key, with the specified value.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
}

x = thisdict.setdefault("trim", "STX")
print(x)                                    #STX

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

#update()
#Inserts the specified items to the dicionary.  The specified items can be dictionary or an iterable object.
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

thisdict.update({"color": "charcoal"})
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

#Copy a Dictionary
#You cannot copy a set simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#copy()
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

newdict = thisdict.copy()
print(newdict)                              #{'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}

#dict()
thisdict = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

newdict = dict(thisdict)
print(newdict)                              #{'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}

#Nested Dictionaries

#A dictionary can also contain many dictionaries.
trucks = {
    "truck1" : {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
    },
    "truck2" : {
    "brand": "Toyota",
    "model": "Tundra",
    "trim": "TRD Pro"
    },
    "truck3" : {
    "brand": "Chevrolet",
    "model": "Silverado",
    "trim": "High Country"
    }
}

print(trucks)                               #{
                                            # 'truck1': {'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}, 
                                            # 'truck2': {'brand': 'Toyota', 'model': 'Tundra', 'trim': 'TRD Pro'}, 
                                            # 'truck3': {'brand': 'Chevrolet', 'model': 'Silverado', 'trim': 'High Country'}
                                            # }

#Separate dictionaries can be nested as children into a parent dictionary
truck1 = {
    "brand": "Ford",
    "model": "F-150",
    "trim": "Raptor"
}

truck2 = {
    "brand": "Toyota",
    "model": "Tundra",
    "trim": "TRD Pro"
}

truck3 = {
    "brand": "Chevrolet",
    "model": "Silverado",
    "trim": "High Country"
}

alltrucks = {
    "truck1": truck1,
    "truck2": truck2,
    "truck3": truck3,
}

print(alltrucks)                            #{
                                            # 'truck1': {'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}, 
                                            # 'truck2': {'brand': 'Toyota', 'model': 'Tundra', 'trim': 'TRD Pro'}, 
                                            # 'truck3': {'brand': 'Chevrolet', 'model': 'Silverado', 'trim': 'High Country'}
                                            # }

#The dict() Constructor
#It is also possibel to use the dict() constructor to make a new dictionary.
thisdict = dict(brand="Ford", model="F-150", trim="Raptor")
print(thisdict)                             #{'brand': 'Ford', 'model': 'F-150', 'trim': 'Raptor'}