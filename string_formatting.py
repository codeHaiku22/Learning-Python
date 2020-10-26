#!/usr/bin/python3

#String format()
#The format() method allows you to format selected parts of a string.
#Sometimes there are parts of a text that you don not control that can come from an external source such as a database or user input.
#To control such values, add placeholders (curly brackets {}) in the text and run the values through the format() method.
price = 49
txt = "The price is {} dollars."

print(txt.format(price))                                        #The price is 49 dollars.

#You can add parameters inside the curly brackets to specify how to convert the value.
price = 49
txt = "The price is {:.2f} dollars."

print(txt.format(price))                                        #The price is 49.00 dollars.

#Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))                  #I want 3 pieces of item number 567 for 49.00 dollars.

#Index Numbers
#You can use index numbers (numbers inside of the curly brackets{}) to be sure the values are placed in the correct placeholders.
quantity= 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, itemno, price))                  #I want 3 pieces of item number 567 for 49.00 dollars.

#If you want to refer to the same value, re-use the index number.
age = 36
name = "John"
txt = "His name is {1}.  {1} is {0} years of age."

print(txt.format(age, name))                                    #His name is John.  John is 36 years of age.

#Named Indexes
#You can also use named indexes by entering a name inside the curly brackets {}, but then you must use names when you pass the parameter values.
myorder = "I have a {carname}, it is a {model}."

print(myorder.format(carname = "Honda", model = "Pilot"))       #I have a Honda, it is a Pilot.