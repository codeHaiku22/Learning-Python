#!/usr/bin/python3

#Generators
"""
Generator functions allow you to declare a function that behaves like an iterator.
Generator functions essentially create a function that can be used in a for loop.
The simplification of code is a result of generator function and generator expression support provided by Python.
Generators are a special type of iterator.
 - Containers like list and set are also iterables. 
 - The uniform way in which all of these are handled adds greatly to the simplification of code.
"""

#The sys module will be imported to help determine the size of the objects throughout this lesson.
import sys

#Let's create a function that represents the first n non-negative integers.
# - Let's assume that each integer takes up a lot of space.

#Build and return a list
#The code builds a full list (nums) into memory
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

list_of_nums = firstn(100)
print(list_of_nums)                                         #[0, 1, 2, 3, 4,...99]

sum_of_first_n = sum(firstn(100))    
print(sum_of_first_n)                                       #4950
print("Size:", sys.getsizeof(firstn(100)))                  #Size: 904

#If we resort to the generator pattern, we no longer need to keep a full list (nums) in memory.
class firstn_class(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn_class(100))        
print(sum_of_first_n)                                       #4950
print("Size:", sys.getsizeof(firstn_class(100)))            #Size: 48

#The generator pattern above is verbose and convoluted.
#It can be rewritten more concisely with a gernator function.
#It is similar to the implementation that built a list in memory, but has the memory usage characteristics of the iterator implementation.
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn_generator(100))
print(sum_of_first_n)                                       #4950
print("Size:", sys.getsizeof(firstn_generator(100)))        #Size: 112

#Size Comparison: function returning list vs. function returning generator
num = 1000000
print("Size:", sys.getsizeof(firstn(num)))                  #Size: 8697456
print("Size:", sys.getsizeof(firstn_generator(num)))        #Size: 112

#Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.
#We can turn a list comprehension into a generator expression by replacing the square brackets ([]) with parenthesis (()).
#Think of a list comprehension as a generator expression wrapped in a list constructor.
# - By allowing generator expressions, a generator function is no longer needed if we do not need the list.
doubles = [2 * n for n in range(25)]      #list comprehension
print(doubles)                                              #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
print("Size:", sys.getsizeof(doubles))                      #Size: 256

doubles = list(2 * n for n in range(25))  #generator expression
print(doubles)                                              #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
print("Size:", sys.getsizeof(doubles))                      #Size: 288

#Generators provide for improved performance with less memory usage.
#We don't need to wait until all elements have been generated to begin to use them.
# - Iterators also provide the same benefit.

#The range() function 
#Returns a list
sum_of_first_n = sum(range(100))
print(sum_of_first_n)                                       #4950
print("Size:", sys.getsizeof(sum_of_first_n))               #Size: 28         

#More Examples:

#Using a for loop
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)                                                    #<generator object mygenerator at 0x7fda130acac0>

for i in g:
    print(i)                                                #1
                                                            #2
                                                            #3

#Using the next iterator
#A generator object will produce a StopIteration once all yield statements have been exhausted.
def mygenerator():
    yield 1
    yield 2
    yield 3   

g = mygenerator()                                                 

value = next(g)                                 
print(value)                                                #1
value = next(g) 
print(value)                                                #2
value = next(g)
print(value)                                                #3
#value = next(g)
#print(value)                                               #StopIteration

#Sorting
#Returns a list of the values sorted in ascending order.
def mygenerator():
    yield 3
    yield 1
    yield 2   

g = mygenerator()                                                 
print(sorted(g))                                            #[1, 2, 3]

#Sum
#Returns the sum of al of the yield items in the generator
def mygenerator():
    yield 1
    yield 2
    yield 3   

g = mygenerator()                                                 
print(sum(g))                                               #6

#Using a while loop in the definition
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
value = next(cd)
print(value)                                                #Starting
                                                            #4
print(next(cd))                                             #3
print(next(cd))                                             #2
print(next(cd))                                             #1
#print(next(cd))                                            #StopIteration

#The Fibonacci Sequence
def fibonacci(limit):
    #0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)

for i in fib:
    print(i)                                                #0
                                                            #1
                                                            #1
                                                            #2
                                                            #3
                                                            #5
                                                            #8
                                                            #13
                                                            #21    

#Print all Even Numbers - Similar to List Comprehension, but parantheses (()) are used.
mygenerator = (i for i in range(10) if i % 2 == 0)

for i in mygenerator:
    print(i)                                                #0
                                                            #2
                                                            #4
                                                            #6
                                                            #8
mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))                                    #[0, 2, 4, 6, 8]                       

#Print all Even Numbers - List Comprehension: square brackets ([]) are used.
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)                                               #[0, 2, 4, 6, 8]

for i in mylist:
    print(i)                                                #0
                                                            #2
                                                            #4
                                                            #6
                                                            #8                                                

#Size Comparison: list vs. generator
mygenerator = (i for i in range(100000) if i % 2 == 0)
mylist = [i for i in range(100000) if i % 2 == 0]

print("Size:", sys.getsizeof(mygenerator))                  #Size: 112
print("Size:", sys.getsizeof(mylist))                       #Size: 406488