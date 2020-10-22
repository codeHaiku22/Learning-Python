#!/usr/bin/python3

#if
a = 33
b = 200

if b > a:
    print("b is greater than a")                #b is greater than a

#elif
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")                  #a and b are equal

#else
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")                #a is greater than b

#else
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")                #a is greater than b

#Short-Hand If
a = 200
b = 33

if a > b: print("a is greater than b")          #a is greater than b

#Short Hand If ... Else
a = 2
b = 330

print("a is greater than b") if a > b else print ("b is greater than a")         #b is greater than a

a = 330
b = 330

print("a is greater than b") if a > b else print ("a is equal to b") if a==b else print ("b is greater than a")         #a is equal to b

#And
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True.")          #Both conditions are True.

#Or
a = 200
b = 33
c = 500

if a > b or c > a:
    print("At least one condition is True.")    #At least one condition is True

#Nested If
x = 41
message = ""

if x > 10:
    message = message + "Above 10"
    if x > 20:
        message = message + " and also above 20!"
    else:
        message = message + ", but not above 20."

print(message)                                  #Above 10 and also above 20!

#pass Statement
#If statements cannot be empty, but if you for some reason have an if statement with no content, put inthe pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass