#!/usr/bin/python3

#Collections are high performance container types within Python.
"""
Counter
namedtuple
OrderedDict
defaultdict
deque
"""

#Counter
#A counter is a dict subclass for counting hashable objects.  
#Counts are allowed to be any integer value inlcuding <=0.
# It is an unordered collection.
#  - Elements are stored as dictionary keys.
#  - Counts are stored as dictionary values.
from collections import Counter

myString = "aaaaabbbbcccdde"
myCounter = Counter(myString)

print(myCounter)                                #Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
print(myCounter.items())                        #dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
print(myCounter.keys())                         #dict_keys(['a', 'b', 'c', 'd', 'e']
print(myCounter.values())                       #dict_values([5, 4, 3, 2, 1])
print(myCounter.most_common(1))                 #[('a', 5)]
print(myCounter.most_common(2))                 #[('a', 5), ('b', 4)]
print(myCounter.most_common(1)[0])              #('a', 5)
print(myCounter.most_common(1)[0][0])           #a
print(myCounter.elements())                     #<itertools.chain object at 0x7fdf18471370>
print(list(myCounter.elements()))               #['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e']

#namedtuple
#Namedtuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
#They can be used wherever regular tuples are used, adding the ability to access fields by name instead of just by position index.
from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)

print(pt)                                       #Point(x=1, y=-4)
print(pt.x, pt.y)                               #1 -4

#OrderedDict
#OrderdDict dictionaries are like regular dictionaries, but they remember the order that items were inserted.
#When iterating over an OrderedDict, the items are returned in the order their keys were first added.
from collections import OrderedDict

ordDict = OrderedDict()
ordDict['a'] = 1
ordDict['b'] = 2
ordDict['c'] = 3
ordDict['d'] = 4
ordDict['e'] = 5
print(ordDict)                                  #OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

ordDict = OrderedDict()
ordDict['d'] = 4
ordDict['a'] = 1
ordDict['c'] = 3
ordDict['e'] = 5
ordDict['b'] = 2
print(ordDict)                                  #OrderedDict([('d', 4), ('a', 1), ('c', 3), ('e', 5), ('b', 2)])

ordDict = {}
ordDict['d'] = 4
ordDict['a'] = 1
ordDict['c'] = 3
ordDict['e'] = 5
ordDict['b'] = 2
print(ordDict)                                  #{'d': 4, 'a': 1, 'c': 3, 'e': 5, 'b': 2}

#defaultdict
#Returns a new dictionary-like object.
#defaultdict is a subclass of the built-in dict class.
# - It overrrides one method and adds one writable instance variable.
# - The remaining funcitonality is the same as for the dict class.
from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)                                        #defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(d['a'])                                   #1     
print(d['b'])                                   #2
print(d['z'])                                   #0

#deque
#Pronounced as "deck", deques are a generalziation of stacks and queues.
#Deques support thread-safe, memory efficient appends and pops from either siede of the deque with apprixmately the same performance in either direction.
# - Though list object support similar operations, they are optimized for fast fixed-length operations and incur memory movements costs for pop and insert operations.
from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
print(d)                                        #deque([1, 2, 3, 4, 5])

d.appendleft(0)
print(d)                                        #deque([0, 1, 2, 3, 4, 5])

d.extend([6,7,8,9])                         
print(d)                                        #deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

d.extendleft([-1,-2])                         
print(d)                                        #deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

d.pop()
print(d)                                        #deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

d.popleft()
print(d)                                        #deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

d.clear()
print(d)                                        #dequeue([])

d.append('a')
d.append('b')
d.append('c')
d.append('d')
d.append('e')
print(d)                                        #deque(['a', 'b', 'c', 'd', 'e'])

d.rotate(1)
print(d)                                        #deque(['e', 'a', 'b', 'c', 'd'])

d.clear()
d.append('a')
d.append('b')
d.append('c')
d.append('d')
d.append('e')
print(d)                                        #deque(['a', 'b', 'c', 'd', 'e'])

d.rotate(3)
print(d)                                        #deque(['c', 'd', 'e', 'a', 'b'])

d.clear()
d.append('a')
d.append('b')
d.append('c')
d.append('d')
d.append('e')
print(d)                                        #deque(['a', 'b', 'c', 'd', 'e'])

d.rotate(-1)
print(d)                                        #deque(['b', 'c', 'd', 'e', 'a'])

d.clear()
d.append('a')
d.append('b')
d.append('c')
d.append('d')
d.append('e')
print(d)                                        #deque(['a', 'b', 'c', 'd', 'e'])

d.rotate(-3)
print(d)                                        #deque(['d', 'e', 'a', 'b', 'c'])