#!/usr/bin/python3

#Python Iterators
#An iterator is an object that contains a countable number of values that can be traversed via iteration.
#Technically, in Python, an iterator is an object which implements the iterator protocol consisting of the methods:
# - __iter__()
# - __next__()

#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects.
# - They are iterable containers which you can get an iterator from.
# - All of these objects have an iter() method which is used to get an iterator.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))                               #apple
print(next(myit))                               #banana
print(next(myit))                               #cherry

#strings
mystr = "kiwi"
myit = iter(mystr)

print(next(myit))                               #k
print(next(myit))                               #i
print(next(myit))                               #w
print(next(myit))                               #i

#Looping Through an Iterator
#The for loop actually creates an iterator object and executes the next() method for each loop.
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)                                    #apple
                                                #banana
                                                #cherry

#strings
mystr = "kiwi"

for x in mystr:                                 
    print(x)                                    #k
                                                #i
                                                #w
                                                #i

#Create an Iterator
"""
To create an object/class as an iterator, you have to implement the methods __iter__() and __next__() to your object.
All classes hav ea function called __init__(), which allows you to do some initializing when the object is being created.
 - The __iter__() method acts similar, you can do operations (initializing, etc.), but must always return the iterator object itself.
 - The __next__() method also allows you to do operations and must return the next item in the sequence. 
"""

#Create an iterator that returns numbers (starting with 1) and each sequence will increase by 1
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))                             #1
print(next(myiter))                             #2    
print(next(myiter))                             #3

#StopIteration
"""
#To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times.
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)                                    #1
                                                #2
                                                #3
                                                #4
                                                #5
