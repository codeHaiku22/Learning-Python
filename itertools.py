#!/usr/bin/python3

#Functions creating iterators for efficient looping.
"""
product
permutations
combinations
accumulate
groupby
Infinite Iterators: count, cycle, repeat
"""

#product
from itertools import product

a = ['red', 'blue']
b = ['shirt', 'pants']

prod = product(a,b)
print(prod)                                     #<itertools.product object at 0x7fc0a07ae800>
print(list(prod))                               #[('red', 'shirt'), ('red', 'pants'), ('blue', 'shirt'), ('blue', 'pants')]

a = ['red', 'blue']
b = ['shirt']

prod = product(a,b)
print(list(prod))                               #[('red', 'shirt'), ('blue', 'shirt')]

prod = product(a,b, repeat=2)
print(list(prod))                               #[('red', 'shirt', 'red', 'shirt'), ('red', 'shirt', 'blue', 'shirt'), ('blue', 'shirt', 'red', 'shirt'), ('blue', 'shirt', 'blue', 'shirt')]

#permutations
from itertools import permutations

a = [1, 2, 3]

perm = permutations(a)
print(list(perm))                               #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2)
print(list(perm))                               #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#combinations
from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]

comb = combinations(a, 2)
print(list(comb))                               #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

combwr = combinations_with_replacement(a, 2)
print(list(combwr))                             #[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

#accumulate
from itertools import accumulate

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)                                        #[1, 2, 3, 4]
print(list(acc))                                #[1, 3, 6, 10]

import operator

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)                                        #[1, 2, 3, 4]
print(list(acc))                                #[1, 2, 6, 24]

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)                                        #[1, 2, 5, 4, 3]
print(list(acc))                                #[1, 2, 5, 5, 5]

#groupby
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)                                #<itertools.groupby object at 0x7fa578019810>

for key, value in group_obj:
    print(key, list(value))                     #True [1, 2]
                                                #False [3, 4, 5]

a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=lambda x: x<3)
print(group_obj)                                #<itertools.groupby object at 0x7fb97a359770>

for key, value in group_obj:
    print(key, list(value))                     #True [1, 2]
                                                #False [3, 4, 5]
persons = [{'name': 'Tim', 'age': 25}, 
           {'name': 'Dan', 'age': 25}, 
           {'name': 'Zina', 'age': 27}, 
           {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])

for key, value in group_obj:
    print(key, list(value))                     #25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
                                                #27 [{'name': 'Zina', 'age': 27}]
                                                #28 [{'name': 'Claire', 'age': 28}]

#Infinite Iterators
from itertools import count, cycle, repeat

#count
#for i in count(10):                             
    #print(i)                                   #10
                                                #11
                                                #12
                                                #...  (to infinity)

for i in count(10):                             
    print(i)                                    #10
    if i == 12:                                 #11
        break                                   #12

#cycle
a = [1, 2, 3]
#for i in cycle(a):  
    #print(i)                                   #1
                                                #2
                                                #3
                                                #1
                                                #2
                                                #3
                                                #...  (endlessly)     

#repeat
#for i in repeat('again'):                       
    #print(i)                                   #again
                                                #again
                                                #again
                                                #...  (endlessly)

for i in repeat('again', 3):                       
    print(i)                                    #again
                                                #again
                                                #again