#!/usr/bin/python3

#The Python random Module
"""
This module implements the pseudo-random number generators for various distributions.
The pseudo-random number generator should not be used for security purposes.
"""
import random

#The random() Method
#Returns a random floating number between 0 and 1
a = random.random()
print(a)                                                        #0.6513070469046051

#The uniform() Method
#Returns a random floating number between the 2 specified numbers (inclusive)
a = random.uniform(1, 10)                   
print(a)                                                        #7.834676322492768

#The random.randint() Method
#Returns a random integer number between the 2 specified numbers (inclusive)
a = random.randint(1, 10)
print(a)                                                        #5

#The random.randrange() Method
#Returns a random number between the given range (inclusive)
a = random.randrange(1, 10)
print(a)                                                        #9

#The third parameter is optional and is used to specify the incrementation (default = 1)
a = random.randrange(1, 10, 3)
print(a)                                                        #7

#The random.normalvariate() Method
#Returns a random float number based on the normal distribution (used in probability theories)
# - The first parameter is the mean.
# - The second parameter is the standard deviation
# - See: https://en.wikipedia.org/wiki/Normal_distribution#/media/File:Normal_Distribution_PDF.svg
a = random.normalvariate(0, 1)
print(a)                                                        #-0.7112243290657954

#The random.choice() Method
#Returns a random element from the given sequence.
mylist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(mylist)                                                   #['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

a = random.choice(mylist)
print(a)                                                        #T

#The random.choices() Method
#Returns a list with a random selection from the given sequence.
#You can weight the possibility of each result with the weights parameter or the cum_weights parameter.
#The sequence can be a string, a range, a list, a tuple, or any other kind of sequence.
#random.choices(<sequence>, [weights=None], [cum_weights=None], [k=1]) 
#Where:
# sequence     A sequence such as a list, a tuple, range of numbers, etc.
# weights      A list where you can weigh the possibility for each value.
# cum_weights  A list where you can weigh the possibility for each value, only this time the possibility is accumulated.
# k            An integer defining the length of the returned list.
mylist = ["apple", "banana", "cherry"]

a = random.choices(mylist)
print(a)                                                        #['banana']

#This list will contain 14 elements and will be 10 times more likelye to select the first element than the other 2.
mylist = ["apple", "banana", "cherry"]

a = random.choices(mylist, weights = [10, 1, 1], k = 14)
print(a)                                                        #['apple', 'cherry', 'apple', 'banana', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'cherry']

#The random.sample() Method
#Returns a list with a dandomly selected selection of a specified number of items from a sequence.
#This method does not change the original sequence.
mylist = ["apple", "banana", "cherry"]

a = random.sample(mylist, 2)
print(a)                                                        #['apple', 'cherry']

#The random.shuffle() Method
#Returns a sequence with the items reorganized from a provided sequence (list, string, or tuple)
#This method changes the original sequence; it does not return a new sequence.
mylist = ["apple", "banana", "cherry"]

random.shuffle(mylist)
print(mylist)                                                   #['cherry', 'banana', 'apple']

#The random.seed() Method
#Initializes the random number generator.
#The random number generator needs a number to start with (seed), to be able to generate a random number.
# - By default, the random number generator uses the current system time.
# - If you use the same seed value, you will get the same random number.
random.seed(10)
print(random.random())                                          #0.5714025946899135
print(random.randint(1,10))                                     #7

random.seed(10)
print(random.random())                                          #0.5714025946899135
print(random.randint(1,10))                                     #7

random.seed(341)
print(random.random())                                          #0.5823101125425785
print(random.randint(1,10))                                     #10

#The Python secrets Module
"""
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as: 
 - passwords
 - account authentication
 - security tokens
 - related secrets
 The secrets module should be used in preference to the default pseudo-random number generator in the random module (designed for modeling and simulation).
 The secretes module provides access to the most secure source of randomness that you operating system provides.
"""
import secrets

#The secrets.randbelow() Method
#Returns a random positive integer below a provided ceiling (exclusive)
a = secrets.randbelow(5)
print(a)                                                        #3

#The secrets.randbits() Method
#Returns a random integer with k random bits.
a = secrets.randbits(3)
print(a)                                                        #5 -> 101

a = secrets.randbits(4)
print(a)                                                        #12 -> 1100

a = secrets.randbits(5)
print(a)                                                        #26 -> 11010

#The secrets.choice() Method
#Returns a random element from the given sequence
mylist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(mylist)                                                   #['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

a = secrets.choice(mylist)
print(a)                                                        #P

#The Python NumPy Module
"""
NumPy (Numeric Python) is a Python module used for working with arrays.
This module also as the ability to produce randomness.
"""
import numpy 

#The numpy.random.rand() Method
#Returns an arry of floating number elements based on the dimensions of the array provided as input parameters. 
#numpy.random.rand([array_dimension0 = 1], [array_dimension2 = 1])
a = numpy.random.rand(3)
print(a)                                                        #[0.89173953 0.70260435 0.52968441]

a = numpy.random.rand(4,2)
print(a)                                                        #[[0.4819947  0.75182633]
                                                                #[0.16571643 0.11128332]
                                                                #[0.51330602 0.60690931]
                                                                #[0.68716757 0.08316626]]

#The numpy.random.randinit() Method
#Returns an arry of integer elements based on the dimensions of the array provided as input parameters. 
#numpy.random.randint(<low>, [high], [size], [dtype])
#Where:
# low    Lowest signed integer to be drawn from the distribution (unless high=None, in which case this parameter is one above the highest such integer).
# high   One above the largest signed integer to be drawn from the distribution (see above for behavior if high=None).
# size   If the given shape is (m, n, k), then m * n * k samples are drawn; default is None in which case as single value is drawn.
# dtype  Desired dtype of the result (int64, int, etc); default is np.int.
a = numpy.random.randint(10)
print(a)                                                        #6

a = numpy.random.randint(1, 100)
print(a)                                                        #93

a = numpy.random.randint(1, 100, 5)
print(a)                                                        #[81 54 31 83 81]

a = numpy.random.randint(1, 100, (3,4))
print(a)                                                        #[[96 68 90 36]
                                                                #[79 47 24 64]
                                                                #[ 3 21  8 84]]

#The numpy.random.shuffle() Method
#Modifies a sequence in-place by shuffling its contents.
#Only shuffles the array along the first axis of a multi-dimensional array.
# - The order of sub-arrays is changed, but their contents remain the same.
arr = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)                                                      #[[1 2 3]
                                                                #[4 5 6]
                                                                #[7 8 9]]

numpy.random.shuffle(arr)
print(arr)                                                      #[[1 2 3]
                                                                #[7 8 9]
                                                                #[4 5 6]]

#The numpy.random.seed() Method
#Initializes the random number generator.
#The random number generator needs a number to start with (seed), to be able to generate a random number.
# - By default, the random number generator uses the current system time.
# - If you use the same seed value, you will get the same random number.
numpy.random.seed(10)
print(numpy.random.random())                                    #0.771320643266746
print(numpy.random.randint(1,10))                               #5
print(numpy.random.rand(3,3))                                   #[[0.49458993 0.44301495 0.83191136]
                                                                #[0.58332174 0.02517173 0.70920801]
                                                                #[0.26556613 0.26360285 0.15037787]]        

numpy.random.seed(10)
print(numpy.random.random())                                    #0.771320643266746
print(numpy.random.randint(1,10))                               #5
print(numpy.random.rand(3,3))                                   #[[0.49458993 0.44301495 0.83191136]
                                                                #[0.58332174 0.02517173 0.70920801]
                                                                #[0.26556613 0.26360285 0.15037787]]

numpy.random.seed(341)
print(numpy.random.random())                                    #0.2651669033704277
print(numpy.random.randint(1,10))                               #4
print(numpy.random.rand(3,3))                                   #[[0.56324107 0.69798339 0.67814787]
                                                                #[0.72276681 0.43686765 0.61625212]
                                                                #[0.13834867 0.10723665 0.7428042 ]]