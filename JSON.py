#!/usr/bin/python3

#Python JSON
#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.

#JSON in Python
#Python has a built-in package called json which can be used to work with JSON data.
#If you have a JSON string, you can parse it by using the json.loads() method.

#Convert JSON to Python (dictionary)
import json

x = '{"name":"John", "age":30, "city":"New York"}'  #sample json

y = json.loads(x)  #parse x into a Python dictionary

print(y["age"])                                                 #30

#Convert Python to JSON String
import json

x = {                    #a Python dict object
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)       #covert x into JSON string

print(y)                                                        #{"name": "John", "age": 30, "city": "New York"}

"""
You can convert Python objects of the following types into JSON strings:
 - dict         converts to         Object
 - list         converts to         Array
 - tuple        converts to         Array
 - string       converts to         String
 - int          converts to         Number
 - float        converts to         Number
 - True         converts to         true
 - False        converts to         false
 - None         converts to         null
"""
import json

print(json.dumps({"name": "John", "age": 30}))                  #{"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))                         #["apple", "bananas"]
print(json.dumps(("apple", "bananas")))                         #["apple", "bananas"]
print(json.dumps("hello"))                                      #"hello"
print(json.dumps(42))                                           #42
print(json.dumps(31.76))                                        #31.76
print(json.dumps(True))                                         #true
print(json.dumps(False))                                        #false
print(json.dumps(None))                                         #null

#Convert a Python object containing all of the legal (allowed) data types
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))                                            #{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], 
                                                                #"pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

#Format the Result

#The json.dumps method has parameters to make it easier to read the result
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))                                  #{
                                                                #    "name": "John",
                                                                #    "age": 30,
                                                                #    "married": true,
                                                                #    "divorced": false,
                                                                #    "children": [
                                                                #        "Ann",
                                                                #        "Billy"
                                                                #    ],
                                                                #    "pets": null,
                                                                #    "cars": [
                                                                #        {
                                                                #            "model": "BMW 230",
                                                                #            "mpg": 27.5
                                                                #        },
                                                                #        {
                                                                #            "model": "Ford Edge",
                                                                #            "mpg": 24.1
                                                                #        }
                                                                #    ]
                                                                #}

#You can also define the separators, the default value is (", " , ": "), which means using a comma and a space to separate each object and a colon and a space to separate keys from values.
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))        #{
                                                                #    "name" = "John".
                                                                #    "age" = 30.
                                                                #    "married" = true.
                                                                #    "divorced" = false.
                                                                #    "children" = [
                                                                #        "Ann". 
                                                                #        "Billy"
                                                                #    ].
                                                                #    "pets" = null.
                                                                #    "cars" = [
                                                                #        {
                                                                #            "model" = "BMW 230".
                                                                #            "mpg" = 27.5
                                                                #        }.
                                                                #        {
                                                                #            "model" = "Ford Edge".
                                                                #            "mpg" = 24.1
                                                                #        }
                                                                #    ]
                                                                #}

#Order the Result
#The json.dumps() method has parameters to order he keys in the result.
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
 
json.dumps(x, indent=4, sort_keys=True)                         #{
                                                                #    "age": 30,
                                                                #    "cars": [
                                                                #        {
                                                                #            "model": "BMW 230",
                                                                #            "mpg": 27.5
                                                                #        },
                                                                #        {
                                                                #            "model": "Ford Edge",
                                                                #            "mpg": 24.1
                                                                #        }
                                                                #    ],
                                                                #    "children": [
                                                                #        "Ann",
                                                                #        "Billy"
                                                                #    ],
                                                                #    "divorced": false,
                                                                #    "married": true,
                                                                #    "name": "John",
                                                                #    "pets": null
                                                                #}

#Dump the information into a file
with open('person.json', 'w') as file:
  json.dump(x, file)

with open('person.json', 'w') as file:
  json.dump(x, file, indent=4)

#Load the information from a file
with open('person.json', 'r') as file:
  person = json.load(file)
  print(person)                                                 #{'name': 'John', 'age': 30, 'married': True, 'divorced': False, 'children': ['Ann', 'Billy'], 
                                                                #'pets': None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.1}]}

#Using a class
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User('Max', 27)

def encode_user(obj):
  if isinstance(obj, User):
      return {'name': obj.name, 'age':obj.age, obj.__class__.__name__: True}
  else:
    raise TypeError

userJSON = json.dumps(user, default=encode_user)
print(userJSON)                                                 #{"name": "Max", "age": 27, "User": true}