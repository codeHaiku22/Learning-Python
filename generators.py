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
print(list_of_nums)                             #[0, 1, 2, 3, 4,...99]

sum_of_first_n = sum(firstn(100))    
print(sum_of_first_n)                           #4950

#If we resort to the generator pattern, we no longer need to keep a full list (nums) in memory.
class firstn(object):
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

sum_of_first_n = sum(firstn(100))        
print(sum_of_first_n)                           #4950

#The generator pattern above is verbose and convoluted.
#It can be rewritten more concisely with a gernator function.
#It is similar to the implementation that built a list in memory, but has the memory usage characteristics of the iterator implementation.
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(100))
print(sum_of_first_n)                           #4950

#Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.
#We can turn a list comprehension into a generator expression by replacing the square brackets ([]) with parenthesis (()).
#Think of a list comprehension as a generator expression wrapped in a list constructor.
# - By allowing generator expressions, a generator function is no longer needed if we do not need the list.
doubles = [2 * n for n in range(25)]      #list comprehension
print(doubles)                                  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

doubles = list(2 * n for n in range(25))  #generator expression
print(doubles)                                  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

#Generators provide for improved performance with less memory usage.
#We don't need to wait until all elements have been generated to begin to use them.
# - Iterators also provide the same benefit.

#The range() function 
#Returns a list
sum_of_first_n = sum(range(100))
print(sum_of_first_n)                           #4950