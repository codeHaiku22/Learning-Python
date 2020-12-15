#!/usr/bin/python3

#ufuncs
"""
The term "ufuncs" stand for "Uiversal Functions" and they are NumPy functions that opera on the ndarray object.
"""

#Why use ufuncs?
"""
They are used to implement vectorization in NumPy which is faster than iteratring over elements.
They also provide broadcasting and additional methods such as reduce, accumulate, etc.
ufuncs take additional parameters:
  where    Boolean array or condition defining where the operations should take place.
  dtype    Defining the return type of elements.
  out      Output array where the return value should be copied.
"""

#---[ Vectorization ]---------------------------------------------------------------------------------------------------------------------------------

#Vectorization is the process of converting iterative statments into a vector-based operation.
#It is faster since modern CPUs are optimized for these types of operations.

#Without ufunc, we can use Python's built-in zip() method.
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)                                                                    #[6, 8, 10, 12]

#With ufunc, we can use the add() function.
import numpy as np
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = np.add(x, y)                                                            #[ 6  8 10 12]

print(z)

#---[ Create Your Own Function ]----------------------------------------------------------------------------------------------------------------------

"""
To create your own ufunc, you have to define a function, like you do with normal functions.
Then, you add it to your NumPy ufunc library with the frompyfunc() method.
The frompyfunc() method takes the following arguments:
  (1) function    The name of the function.
  (2) inputs      The number of input arguments (arrays).
  (3) outputs     The number of output arrays.
"""
import numpy as np

#Create your own ufunc for addition
def myAdd(x, y):
    return x + y

myAdd = np.frompyfunc(myAdd, 2, 1)    

print(myAdd([1, 2, 3, 4], [5, 6, 7, 8]))                                    #[6 8 10 12]

#Check if a function is a ufunc.
# - If it is, it should return <class 'numpy.ufunc'>
# - If it is not, it should return <class 'function'>
# - If it is not recognized, it will return an error
print(type(np.add))                                                         #<class 'numpy.ufunc'>
print(type(np.concatenate))                                                 #<class 'function'>
#print(type(np.blahblah))                                                   #AttributeError: module 'numpy' has no attribute 'blahblah'

#Use an if statement to check if the function is a ufunc or not.
if type(np.add) == np.ufunc:
    print('add is ufunc')                                                   #add is ufunc
else:
    print('add is not ufunc')

#---[ Simple Arithmetic ]-----------------------------------------------------------------------------------------------------------------------------

"""
You could use arithmetic operators (+, -, *, /) directly between NumPy arrays, but we can also use functions that take any array-like objects and performs arithmetic conditionally.
Arithmetic Conditionally means that we can define conditions where the arithmetic operation should happen.
All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
"""

import numpy as np

#Addition
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)

print(newarr)                                                               #[30 32 34 36 38 40]

#Subtraction
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)

print(newarr)                                                               #[-10  -1   8  17  26  35]

#Multiplication
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)

print(newarr)                                                               #[ 200  420  660  920 1200 1500]

#Division
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.divide(arr1, arr2)

print(newarr)                                                               #[0.5        0.95238095 1.36363636 1.73913043 2.08333333 2.4       ]

#Power
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)

print(newarr)                                                               #[         1000       3200000     729000000 6553600000000          2500
                                                                            #             0]

#Remainder - mod() and remainder()
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr1 = np.mod(arr1, arr2)
newarr2 = np.remainder(arr1, arr2)

print(newarr1)                                                              #[ 1  6  3  0  0 27]
print(newarr2)                                                              #[ 1  6  3  0  0 27]

#Quotient and Mod
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)

print(newarr)                                                               #(array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))

#Absolute Values
# - Both the absolute() and abs() functions functions do the same operation element-wise
# - We should use absolute() to avoid confusion with python's inbuilt math.abs() 
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)

print(newarr)                                                               #[1 2 1 2 3 4]

#---[ Rounding Decimals ]-----------------------------------------------------------------------------------------------------------------------------

"""
There are primarily 5 ways of rounding decimals in NumPy:
  (1) truncation
  (2) fix
  (3) rounding
  (4) floor
  (5) ceil
"""

import numpy as np

#Truncation - trunc() and fix()
# - Remove the decimals and return the number closest to 0.
arr1 = np.trunc([-3.1666, 3.6667])
arr2 = np.fix([-3.1666, 3.6667])

print(arr1)                                                                 #[-3.  3.]
print(arr2)                                                                 #[-3.  3.]

#Rounding - around()
# - Increment preceding digit or decimal by 1 if >=5, else do nothing.
arr = np.around(3.1666, 2)

print(arr)                                                                  #3.17

#Floor - floor()
# - Round off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])

print(arr)                                                                  #[-4.   3.]

#Ceiling - ceil()
# - Round off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])

print(arr)                                                                  #[-3.  4.]

#---[ Logs ]------------------------------------------------------------------------------------------------------------------------------------------

"""
NumPy provides functions to perform log at the base 2, e (Natural Log),  and 10.
We will also explore how we can take log for any base by creating a custom ufunc.
All of the log functions will place -inf or inf in the elements if the log can not be computed.
"""

import numpy as np

#Log at Base 2 - log2()
# - The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
arr = np.arange(1, 10)

print(np.log2(arr))                                                         #[0.         1.         1.5849625  2.         2.32192809 2.5849625
                                                                            # 2.80735492 3.         3.169925  ]

#Log at Base 10 - log10()
# - The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
arr = np.arange(1, 10)

print(np.log10(arr))                                                        #[0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125
                                                                            # 0.84509804 0.90308999 0.95424251]

#Natural Log - Log at Base e - log()
# - The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
arr = np.arange(1, 10)

print(np.log(arr))                                                          #[0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947
                                                                            # 1.94591015 2.07944154 2.19722458]

#Log at Any Base
# - NumPy does not provide any function to take log at any base
# - We can use the frompyfunc() function along with inbuilt function math.log() with 2 input parameters and 1 output parameter.
from math import log

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))                                                       #1.7005483074552052

#---[ Summations ]------------------------------------------------------------------------------------------------------------------------------------

"""
While addition is done between two arguments, summation happens over n elements.
"""

import numpy as np

#Sum the values in arr1 and the values in arr2
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])

print(newarr)                                                               #12

#Summation Over an Axis
# - If you specify axis=1, NumPy will sum the numbers in each array.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr_axis0 = np.sum([arr1, arr2], axis=0)
arr_axis1 = np.sum([arr1, arr2], axis=1)

print(arr_axis0)                                                            #[2 4 6]
print(arr_axis1)                                                            #[6 6]

#Cumulative Sum - cumsum()
# - Partially add the elements in the array
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)

print(newarr)                                                               #[1 3 6]

#---[ Products ]--------------------------------------------------------------------------------------------------------------------------------------

"""
To find the product of the elements in an array, use the prod() function.
"""

import numpy as np

#Find the product of the elements of 1 array
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)

print(x)                                                                    #24

#Find the product of the elements of 2 arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])

print(x)                                                                    #40320

#Product Over an Axis
# - If you specify axis=1, NumPy will return the product of each array.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr_axis0 = np.prod([arr1, arr2], axis=0)
arr_axis1 = np.prod([arr1, arr2], axis=1)

print(arr_axis0)                                                            #[ 5 12 21 32]
print(arr_axis1)                                                            #[  24 1680]

#Cumulative Product - cumprod()
# - Partially take the product of the elements in the array
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)

print(newarr)                                                               #[   5   30  210 1680]

#---[ Differences ]-----------------------------------------------------------------------------------------------------------------------------------

"""
A discrete difference means subtracting two successive elements.
 - For [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
To find the discrete difference, use the diff() function.
"""

import numpy as np

#Compute discrete difference of the array
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)

print(newarr)                                                               #[  5  10 -20]

#We can perform this operation repeatedly by giving parameter n.
# - For [1, 2, 3, 4] the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1], 
#    + Then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0] 
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)       #[15-10, 25-15, 5-25] = [5, 10, -20]
                                 #[10-5, -20-10] = [5 -30]
print(newarr)                                                               #[  5 -30]

#---[ LCM - Lowest/Least Common Multiple ]------------------------------------------------------------------------------------------------------------

"""
The LCM is the lowest/least number that is a common multiple of 2 or more numbers.
"""

import numpy as np

#Find the LCM of 2 numbers.
num1 = 4
num2 = 6
x = np.lcm(num1, num2)

print(x)                                                                    #12

#Finding LCM in Arrays - reduce()
# - The reduce() method is used when finding the LCM of arrays.
# - The reduce() method will use the ufunc, in this case the lcm() function, on each element and reduce the array by 1 dimension.
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)

print(x)                                                                    #18

#Find the LCM of all of an array where the array contains all integers from 1 to 10.
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)

print(x)                                                                    #2520

#---[ GCD - Greatest Common Denominator ]-------------------------------------------------------------------------------------------------------------

"""
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
"""

import numpy as np

#Find the GCD of 2 numbers.
num1 = 6
num2 = 9
x = np.gcd(num1, num2)

print(x)                                                                    #3

#Finding GCD in Arrays - reduce()
# - The reduce() method is used when finding the GCD of arrays.
# - The reduce() method will use the ufunc, in this case the gcd() function, on each element and reduce the array by 1 dimension.
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)

print(x)                                                                    #4

#---[ Trigonometric ]---------------------------------------------------------------------------------------------------------------------------------

"""
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
By default all of the trigonometric functions take radians as parameters.
 - Radian values are pi/180 * degree values
"""

import numpy as np

#Find sine value of PI/2:
x = np.sin(np.pi/2)

print(x)                                                                    #1.0

#Find sine values for all of the values in an array.
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)

print(x)                                                                    #[1.         0.8660254  0.70710678 0.58778525]

#Convert Degrees to Radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)

print(x)                                                                    #[1.57079633 3.14159265 4.71238898 6.28318531]

#Convert Radians to Degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)

print(x)                                                                    #[ 90. 180. 270. 360.]

#Finding Angles
# - Finding angles from values of sine, cos, tan. (sin, cos and tan inverse (arcsin, arccos, arctan) )
# - NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

#Find the angle of 1.0
x = np.arcsin(1.0)

print(x)                                                                    #1.5707963267948966

#Angles of Each Value in Arrays
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)

print(x)                                                                    #[ 1.57079633 -1.57079633  0.10016742]

#Hypotenuse - hypot()
# - NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenuse based on the Pythagorean Theorum.
base = 3
perp = 4
x = np.hypot(base, perp)

print(x)                                                                    #5.0

#---[ Hyperbolic ]------------------------------------------------------------------------------------------------------------------------------------

"""
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values.
"""

import numpy as np

#Find sinh value of PI/2:
x = np.sinh(np.pi/2)

print(x)                                                                    #2.3012989023072947

#Find cosh values for all of the values in an array.
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)

print(x)                                                                    #[2.50917848 1.60028686 1.32460909 1.20397209]

#Finding Angles
# - Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
# - Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

#Find the angle of 1.0
x = np.arcsinh(1.0)

print(x)                                                                    #0.881373587019543

#Angles of Each Value in Arrays
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)

print(x)                                                                    #[0.10033535 0.20273255 0.54930614]

#---[ Set Operations ]--------------------------------------------------------------------------------------------------------------------------------

"""
A set in mathematics is a collection of unique elements.
Sets are used for operations involving frequent intersection, union, and difference operations.
"""

import numpy as np

#Create Sets in NumPy - unique()
# - We can use NumPy's unique() method to find unique elements from any array. 
#    + Create a set array, but remember that the set arrays should only be 1-D arrays.
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)

print(x)                                                                    #[1 2 3 4 5 6 7]

#Finding Union - union1d()
# - To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)

print(newarr)                                                               #[1 2 3 4 5 6]

#Finding Intersection - intersect1d()
# - To find only the values that are present in both arrays, use the intersect1d() method.
# - The intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. 
#    + It should always be set to True when dealing with sets.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)                                                               #[3 4]

#Finding Difference - setdiff1d()
# - To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
# - The setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. 
#    + It should always be set to True when dealing with sets.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)                                                               #[1 2]

#Finding Symmetric Difference - setxor1d()
# - To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
# - The setxor1d() method takes an optional argument assume_unique, which if set to True can speed up computation. 
#    + It should always be set to True when dealing with sets.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)                                                               #[1 2 5 6]