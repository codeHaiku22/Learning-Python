#!/usr/bin/python

#Old School String Formatting
"""
Before Python 3.6, you had 2 main ways of embedding Python expressions inside string literals for formatting:
 - % formatting
 - str.format()
"""
#% formatting
name = "Eric"
print('Hello, %s.' % name)                                                                          #Hello, Eric.

name = "Eric"
age = 74
print('Hello, %s. You are %s years old.' % (name, age))                                             #Hello, Eric. You are 74 years old.

#Why % formatting is not great
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "Comedian"
affiliation = "Monty Python"
print("Hello, %s %s. You are %s years old. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation))   #Hello, Eric Idle. You are 74 years old.  You are a Comedian.  You were a member of Monty Python.

#str.format()
name = "Eric"
age = 74
print("Hello, {}. You are {} years old.".format(name, age))                                         #Hello, Eric. You are 74 years old.

name = "Eric"
age = 74
print("Hello, {1}. You are {0} years old.".format(age, name))                                       #Hello, Eric. You are 74 years old.

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age} years old.".format(name=person['name'], age=person['age']))     #Hello, Eric. You are 74 years old.     

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age} years old.".format(**person))                                   #Hello, Eric. You are 74 years old.

#Why str.format() is not great
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "Comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age} years old. " + 
       "You are a {profession}. You were a member of {affiliation}.") \
       .format(first_name=first_name, last_name=last_name, age=age, \
               profession=profession, affiliation=affiliation))                                     #Hello, Eric Idle. You are 74 years old. You are a Comedian. You were a member of Monty Python.


#Introducing f-strings: A New and Improved Way to Format Strings in Python
"""
Also called "formatting string literals", 
f-strings are string literals that have an f at the beginning and curly braces ({}) containing expressions that will be replaced with their values.
Their expressions are evaluated at runtime and formatted using the __format__ protocol.
"""
#Simple Syntax
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age} years old.")                                                   #Hello, Eric. You are 74 years old.
print(F"Hello, {name}. You are {age} years old.")                                                   #Hello, Eric. You are 74 years old.

#Arbitrary Expressions
#Since f-string are evaulated at runtme, you can put any and all valid Python expressions in them.
print(f"{2 * 37}")                                                                                  #74

#You can also call functions.
def to_lowercase(input):
    return input.lower()

name = 'Eric Idle'
print(f"{to_lowercase(name)} is a funny guy.")                                                      #eric idle is a funny guy.

#You also have the option of calling a method directly.
name = 'Eric Idle'
print(f"{name.lower()} is a funny guy.")                                                            #eric idle is a funny guy.

#You could even use objects created from classes with f-strings.
#The __str__() and __repr__() methods deal with how objects are presented as strings.
# - You must include include at least 1 of these methods in the class definition.
# - The __repr__() is superior since it can be used in palce of __str__().
# - The string returned by __str__() is the informal string representation of an object and should be readable.
# - The string returned by __repr__() is the official representation an should be unambiguous.
# - Calling str() and repr() is preferable to using __str__() and __repr__() directly.
# - By default, f-strings will use __str__(), but you can make sure they use __repr__() with the "!r" conversion flag.
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")                                                                            #Eric Idle is 74 years old.
print(f"{new_comedian!r}")                                                                          #Eric Idle is 74 years old. Surprise!

#Multiline f-Strings
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "Comedian"
affiliation = "Monty Python"

message1 = (
    f"Hi {name}. "
    f"You are {age} years old. "
    f"You are a {profession}. "
    f"You were a member of {affiliation}."
)

print(message1)                                                                                      #Hi Eric Idle. You are 74 years old. You are a Comedian. You were a member of Monty Python.

message2 = f"Hi {name}. " \
           f"You are {age} years old. " \
           f"You are a {profession}. " \
           f"You were a member of {affiliation}."

print(message2)                                                                                     #Hi Eric Idle. You are 74 years old. You are a Comedian. You were a member of Monty Python.

#Python f-Strings: The Pesky Details

#Quotation Marks
#You can use various types of quotation marks.
#Just be sure you are not using the same type of quotation mark on the outside of the f-string as you are using in the expression.
n = f"{'Eric Idle'}"
print(n)                                                                                            #Eric Idle

n = f'{"Eric Idle"}'
print(n)                                                                                            #Eric Idle

n = f"""Eric Idle"""
print(n)                                                                                            #Eric Idle

n = f'''Eric Idle'''
print(n)                                                                                            #Eric Idle

name = "Eric"
age = 74
n = f"The \"comedian\" named {name} is {age} years old."
print(n)                                                                                            #The "comedian" named Eric is 74 years old.

#Dictionaries
#If you are going to use single quotation marks ('') for the keys, you must use double quotation marks ("") for the f-string containing the keys.
comedian = {'name': 'Eric Idle', 'age': 74}
n = f"The comedian is {comedian['name']} and he is {comedian['age']} years old."
print(n)                                                                                            #The comedian is Eric Idle and he is 74 years old.

#Braces
#In order to make a brace appear in your string, you must use double braces ({{}}).
n = f"{{70 + 4}}"
print(n)                                                                                            #{70 + 4}

#Triple braces ({{{}}}) will result in there being only single braces ({}).
n = f"{{{70 + 4}}}"
print(n)                                                                                            #{74}

#You can get more braces to show if you use moer than triple braces.
n = f"{{{{70 + 4}}}}"
print(n)                                                                                            #{{70 + 4}}

#Backslashes
#You can use backslash (\) escapes in the string portion of an f-string, but not as escapes in the expression part of an f-string.
#n = f"{\"Eric Idle\"}"
#print(n)                                                                                           #Syntax Error: f-string expression part cannot include a backslash

#You can work around this by evaulating the expression beforehand and using the result in the f-string.
name = "Eric Idle"
n = f"{name}"
print(n)                                                                                            #Eric Idle

#Inline Comments
#Expressions should not include comments using the # symbol.
#n = f"Eric is {2 * 37 #Oh my!}."
#print(n)                                                                                           #SyntaxError: f-string expression part cannot include '#'