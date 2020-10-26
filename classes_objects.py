#!/usr/bin/python3

#Python Classes/Objects
"""
Python is an object-oriented programming language.
Almost everything in Python is an object with respective properties and methods.
A class is like an object constructor or a "blueprint" for creating objects.
"""
#Create a Class
#Use the keyword class to create a class.
class MyClass:
    x = 5

#Create an Object
#Use the MyClass class to create an object
p1 = MyClass()    
print(p1.x)                                     #5

#The __init__() Function
#The examples above are classes and objects in their simplest form and are not really useful in real-life applications.
"""
To understand the meaning of classes, we hav to understand the built-in __init__() function.
All classes have a function called __init__() which is always executed whenthe class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
The __init__() function is called automatically every time the class is being used to create a new object.
The self parameter is a reference to the current instance of the class and is used to acces variables that belong to the class.
"""

#Create a class named Person and use the __init__() function to assign values for name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)                                  #John
print(p1.age)                                   #36

#Object Methods
#Objects can also contain methods.
# - Methods in objects are functions that belong to the object.

#Insert a function that prints a greeting and execute it on the p1 object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name + ".")       

p1 = Person("John", 36)
p1.myfunc()                                     #Hello, my name is John.

#The self Parameter
#The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.
#It does not have to be named "self"; you can name it whatever you like, but it has to be the first parameter of any function in the class.

#Use the words "mySillyObject" and "abc" instead of "self".
class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name + ".")

p1 = Person("John", 36)
p1.myfunc()                                     #Hello, my name is John.

#Modify Object Properties
#You can modify properties on ojects.
class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name + ".")

p1 = Person("John", 36)                         
p1.myfunc()                                     #Hello, my name is John.

p1.name = "Paul"
p1.myfunc()                                     #Hello, my name is Paul.

#Delete Object Properties
#You can delete objects by using the del keyword.
class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name + ".")

p1 = Person("John", 36)                         
del p1

#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
    pass

#Python Inheritance
"""
Inheritance allows us to define a class that inherits all of the methods and properties from another class.
  - Parent class is the class being inherited from (also known as the base class).
  - Child class is the class the inheirs from another class (also known as the derived class).
"""

#Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()                                   #John Doe

#Create a Child Class
#To create a class that inherits functionality from another class, sent the parent class as a parameter when creating the child class.
#The pass keyword is used since we are not adding any additional properties or methods.
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()                                   #Mike Olsen

#Use the __init__() function
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fullname = fname + " " + lname

x = Student("Ronin", "Grewal")
print(x.fullname)                               #Ronin Grewal

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#Use the super() Function
#Python also has a super function that will make the child inherit all of the methods and properties from its parent.
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#Add Properties
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2020)

#Add Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome,", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2020)        
x.welcome()                                     #Welcome, Mike Olsen to the class of 2020
