#!/usr/bin/python3

#NumPy (Numerical Python)
"""
Used for working with arrays
Also contains functions for linear algebra, fourier transform, and matrices
Created in 2005 by Travis Oliphant as an open source project
NumPy arrays (ndarray) are up to 50x faster than traditional Python lists
 - Optimized to work with the latest CPU architectures
 - Unlike lists, Numpy arrays are stored at one continuous place in memory - locality of reference.
"""

import numpy as np

#---[ Creating Arrays ]-------------------------------------------------------------------------------------------------------------------------------

#Check numpy version
print(np.__version__)                                                       #1.19.4

#Create a NumPy ndarray object

#list to ndarray
arr = np.array([1, 2, 3, 4, 5])
print(arr)                                                                  #[1 2 3 4 5]
print(type(arr))                                                            #<class 'numpy.ndarray'>

#tuple to ndarray
arr = np.array((1, 2, 3, 4, 5))
print(arr)                                                                  #[1 2 3 4 5]
print(type(arr))                                                            #<class 'numpy.ndarray'>

#---[ Dimensions in Arrays ]--------------------------------------------------------------------------------------------------------------------------

#A dimension in an array is one level of array depth (nested arrays).

#0-D arrays
arr = np.array(42)
print(arr)                                                                  #42

#1-D arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)                                                                  #[1 2 3 4 5]

#2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)                                                                  #[[1 2 3]
                                                                            # [4 5 6]]

#3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])                                            
print(arr)                                                                  #[[[1 2 3]
                                                                            #  [4 5 6]]
                                                                            #
                                                                            # [[1 2 3]
                                                                            #  [4 5 6]]]

#Determine number of dimensions of an array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)                                                               #0
print(b.ndim)                                                               #1
print(c.ndim)                                                               #2
print(d.ndim)                                                               #3

#Higher dimensional arrays
#An array can have any number of dimensions which can be set using the ndmin argument.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)                                                                  #[[[[[1 2 3 4]]]]]
print('Number of dimensions:', arr.ndim)                                    #Number of dimensions: 5

#---[ Array Indexing ]--------------------------------------------------------------------------------------------------------------------------------

#1-D arrays
arr = np.array([1, 2, 3, 4])
print(arr[0])                                                               #1
print(arr[1])                                                               #2
print(arr[2] + arr[3])                                                      #7

#[1, 2, 3, 4]
# -  -  -  -

#2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Second elements on 1st dimension:', arr[0,1])                        #Second element on 1st dimension: 2
print('Fifth element on 2nd dimension:', arr[1, 4])                         #Fifth element on 2nd dimension: 10

#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#  -  -  -  -  -    -  -  -  -  --  
# ---------------  ---------------- 

#3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('Third element on 2nd dimension of 1st dimension:', arr[0, 1, 2])     #Third element on 1st dimension of second array: 6

#[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
#   -  -  -    -  -  -      -  -  -    --  --  --   
#  ---------  ---------    ---------  ------------   
# ----------------------  -------------------------    

#Negative ondexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dimension:', arr[1, -1])                       #Last element from second dimension: 10

#---[ Array Slicing ]---------------------------------------------------------------------------------------------------------------------------------

#Slicing an array means to take elements from one index to another index: [start:end:step]
# - If we don't pass start, it is defaulted to 0.
# - If we don't pass end, it is defaulted to the length of the array in that dimension.
# - If we don't pass step, it is defaulted to 1.

#1-D arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])                                                             #[2 3 4 5]
print(arr[4:])                                                              #[5 6 7]
print(arr[:4])                                                              #[1 2 3 4]
print(arr[3:-1])                                                            #[4 5 6]
print(arr[-3:-1])                                                           #[5 6]
print(arr[1:5:2])                                                           #[2 4]
print(arr[::2])                                                             #[1 3 5 7]

#2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0, 1:4])                                                          #[2 3 4]
print(arr[1, 1:4])                                                          #[7 8 9]
print(arr[0:2, 2])                                                          #[3]
print(arr[0:2, 2])                                                          #[3 8]
print(arr[0:2, 1:4])                                                        #[[2 3 4]
                                                                            # [7 8 9]]

#---[ NumPy Data Types ]------------------------------------------------------------------------------------------------------------------------------

#Python has the following data types:
# string
# integer
# float
# boolean
# complex

#NumPy as the following data types:
# i  integer
# b  boolean
# u  unsigned integer
# f  float
# c  complex float
# m  timedelta
# M  datetime
# O  object
# S  string
# U  unicode string
# V  fixed chunk of memory for another type (void)

#dtype property - Checking the data type of an array
arr = np.array([1, 2, 3, 4])
print(arr.dtype)                                                            #int64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)                                                            #<U6

#dtype argument - Creating arrays with a defined data type
arr = np.array([1, 2, 3, 4], dtype='S')                                 
print(arr)                                                                  #[b'1' b'2' b'3' b'4']
print(arr.dtype)                                                            #|S1

#For i, u, f, S, and U we can define the size

#Create an array with that has a data type of a 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)                                                                  #[1 2 3 4]
print(arr.dtype)                                                            #int32

#What if a value cannot be converted?
#arr = np.array(['a', '2', '3'], dtype='i')                                 #ValueError: invalid literal for int() with base 10: 'a'

#astype function - Converting data type on existing arrays
arr = np.array([1.1, 2.1, 3.1])

newarr0 = arr.astype('i')
print(newarr0)                                                               #[1 2 3]
print(newarr0.dtype)                                                         #int32

newarr1 = arr.astype('int')
print(newarr1)                                                               #[1 2 3]
print(newarr1.dtype)                                                         #int64

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)
print(newarr)                                                               #[ True False  True]
print(newarr.dtype)                                                         #bool

#---[ Copy vs. View ]---------------------------------------------------------------------------------------------------------------------------------

#The main difference betwen a copy and a view of an array is that the copy is a new array and the view is just a view of the original array.
# - The copy owns the data and any changes made to the copy will not affect the original array and vice-versa.
# - The view does not own the data and any changes ade to the view will affect the original data and vice-versa.

#copy() - Copying an array
orig = np.array([1, 2, 3, 4, 5])
copy = orig.copy()

orig[0] = 42

print(orig)                                                                 #[42  2  3  4  5]
print(copy)                                                                 #[1 2 3 4 5]

#view() - Viewing an array
orig = np.array([1, 2, 3, 4, 5])
view = orig.view()

orig[0] = 31

print(orig)                                                                 #[31  2  3  4  5]
print(view)                                                                 #[31  2  3  4  5]

#Check if an array owns it's data - is it a copy or a view?
#Every NumPy array has the attribute base that returns None if the array owns the data, otherwise the base attribute refers to the original object.
orig = np.array([1, 2, 3, 4, 5])
copy = orig.copy()
view = orig.view()

print(copy.base)                                                            #None
print(view.base)                                                            #[1 2 3 4 5]

#---[ Array Shape ]-----------------------------------------------------------------------------------------------------------------------------------

#The shape of an array is the number of elements in each dimension.
#shape attribute - returns a tuple with each index having the number of corresponding elements.

#Get shape of a 2-dimensional array with 4 elements in each dimension
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)                                                            #(2, 4)

#Get shape of a 5-dimensional array 
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)                                                                  #[[[[[1 2 3 4]]]]]
print(arr.shape)                                                            #(1, 1, 1, 1, 4)

#---[ Array Reshaping ]-------------------------------------------------------------------------------------------------------------------------------

#To reshape is to change the shape of an array.
# - By reshaping, we can add or remove dimensions of change the number of elements in each dimension.
# - Any reshape can occur as long as the elements required for reshaping are equal in both shapes

#Reshape from 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)

print(newarr)                                                               #[[ 1  2  3]
                                                                            # [ 4  5  6]
                                                                            # [ 7  8  9]
                                                                            # [10 11 12]]

#Reshape from 1-D to 3-D                                                                            
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)

print(newarr)                                                               #[[[ 1  2]
                                                                            #  [ 3  4]
                                                                            #  [ 5  6]]
                                                                            #
                                                                            # [[ 7  8]
                                                                            #  [ 9 10]
                                                                            #  [11 12]]]

#Reshaping returns the original array: creates a view (not a copy) 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4)

print(newarr.base)                                                          #[1 2 3 4 5 6 7 8]

#Unknown dimension
# - You are allowed to have only 1 unknown dimension.
# - You don't have to specify an exact number for 1 of the dimensions in the reshape method, just pass -1 and NumPy will calculate for you.

#Convert 1-D array with 8 elements to 3-D array with 2x2 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)

print(newarr)                                                               #[[[1 2]
                                                                            #  [3 4]]
                                                                            #
                                                                            # [[5 6]
                                                                            #  [7 8]]]

#Flattening arrays 
# - Converting a multidimensional array into a 1-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)

print(newarr)                                                               #[1 2 3 4 5 6]

#Note: There are a lot of functions for changing the shapes of arrays in numpy: flatten, ravel 
#      There are also functions for rearranging the elements: rot90, flip, fliplr, flipud, etc. 
#      These fall under Intermediate to Advanced section of numpy.

#---[ Iterating Arrays ]------------------------------------------------------------------------------------------------------------------------------

#1-D arrays
arr = np.array([1, 2, 3])

for x in arr:
    print(x)                                                                #1
                                                                            #2
                                                                            #3

#2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])                                                                            

for x in arr:
    print(x)                                                                #[1 2 3]
                                                                            #[4 5 6]

for x in arr:
    for y in x:
        print(y)                                                            #1
                                                                            #2
                                                                            #3
                                                                            #4
                                                                            #5
                                                                            #6                                                                            

#3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)                                                                #[[1 2 3]
                                                                            # [4 5 6]]
                                                                            #[[ 7  8  9]
                                                                            # [10 11 12]]

for x in arr:
    for y in x:
        print(y)                                                            #[1 2 3]                                                
                                                                            #[4 5 6]
                                                                            #[7 8 9]
                                                                            #[10 11 12]

for x in arr:
    for y in x:
        for z in y:
            print(z)                                                        #1
                                                                            #2
                                                                            #3
                                                                            #4
                                                                            #5
                                                                            #6
                                                                            #7
                                                                            #8
                                                                            #9
                                                                            #10
                                                                            #12

#nditer() function

#Iterate each scalar element
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)                                                                #1    
                                                                            #2
                                                                            #3
                                                                            #4
                                                                            #5
                                                                            #6
                                                                            #7
                                                                            #8

#Iterate with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)                                                                #1
                                                                            #3
                                                                            #5
                                                                            #7

#op_dtypes argument - Iterate array with different data types
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)                                                                #b'1'
                                                                            #b'2'
                                                                            #b'3'
                                                                            #b'4'

#ndenumerate() method - Enumerated iteration

#1-D arrays
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)                                                           #(0,) 1
                                                                            #(1,) 2
                                                                            #(2,) 3

#2-D arrays
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)                                                           #(0, 0) 1
                                                                            #(0, 1) 2
                                                                            #(0, 2) 3
                                                                            #(0, 3) 4
                                                                            #(1, 0) 5
                                                                            #(1, 1) 6
                                                                            #(1, 2) 7
                                                                            #(1, 3) 8

#---[ Joining Arrays ]--------------------------------------------------------------------------------------------------------------------------------

#Arrays are joined by axes.

#concatenate() function
#We pass a sequence of arrays we want to join to the concatenate() function along with the axis (if not specified, defaults to 0).

#1-D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

print(arr)                                                                  #[1 2 3 4 5 6]

#2-D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2))
print(arr)                                                                  #[[1 2]
                                                                            # [3 4]
                                                                            # [5 6]
                                                                            # [7 8]]

arr = np.concatenate((arr1, arr2), axis=1)                          
print(arr)                                                                  #[[1 2 5 6]
                                                                            #[3 4 7 8]]     

#stack() function
#Similar to concatenate(), the only difference is that stacking is done along a new axis.
# - We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other (stacking).
# - We pass a sequence of arrays that we want to join to stack() method along with the axis (if not specified, defaults to 0).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2))
print(arr)                                                                  #[[1 2 3]
                                                                            # [4 5 6]]

arr = np.stack((arr1, arr2), axis=1)
print(arr)                                                                  #[[1 4]
                                                                            # [2 5]
                                                                            # [3 6]]

#hstack() function - Stacking along rows                                                                            
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr)                                                                  #[1 2 3 4 5 6]

#vstack() function - Stacking along columns                                                                            
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
print(arr)                                                                  #[[1 2 3]
                                                                            # [4 5 6]]

#dstack() function - Stacking along height (depth)                                 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
print(arr)                                                                  #[[[1 4]
                                                                            #  [2 5]
                                                                            #  [3 6]]]

#---[ Splitting Arrays ]------------------------------------------------------------------------------------------------------------------------------

#Splitting breaks one array into multiple
#There is a split() method available, bit it won't adjust the elements when the elements are less in the source array for splitting.

#array_split() function
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)

print(newarr)                                                               #[array([1, 2]), array([3, 4]), array([5]), array([6])]

#Split into arrays

#1-D arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)

print(newarr[0])                                                            #[1 2]
print(newarr[1])                                                            #[3 4]
print(newarr[2])                                                            #[5 6]

#2-D arrays
arr = ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)

print(newarr)                                                               #[array([[1, 2],
                                                                            #       [3, 4]]), array([[5, 6],
                                                                            #       [7, 8]]), array([[ 9, 10],
                                                                            #       [11, 12]])]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = np.array_split(arr, 3)

print(newarr)                                                               #[array([[1, 2, 3],
                                                                            #       [4, 5, 6]]), array([[7, 8, 9]]), array([[10, 11, 12]])]
#Specify an axis
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = np.array_split(arr, 3, axis=1)

print(newarr)                                                               #[array([[ 1],
                                                                            #       [ 4],
                                                                            #       [ 7],
                                                                            #       [10]]), array([[ 2],
                                                                            #       [ 5],
                                                                            #       [ 8],
                                                                            #       [11]]), array([[ 3],
                                                                            #       [ 6],
                                                                            #       [ 9],
                                                                            #       [12]])]                                                                

#hsplit() function - Splitting along rows                                                                            
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = np.hsplit(arr, 3)

print(newarr)                                                               #[array([[ 1],
                                                                            #       [ 4],
                                                                            #       [ 7],
                                                                            #       [10]]), array([[ 2],
                                                                            #       [ 5],
                                                                            #       [ 8],
                                                                            #       [11]]), array([[ 3],
                                                                            #       [ 6],
                                                                            #       [ 9],
                                                                            #       [12]])]

#vsplit() function - Splitting along columns                                                                            
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = np.vsplit(arr, 4)

print(newarr)                                                               #[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]]), array([[10, 11, 12]])]

#dsplit() function - splitting along height (depth)                                 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
newarr = np.dsplit(arr, 1)

print(newarr)                                                               #[array([[[ 1,  2,  3],
                                                                            #        [ 4,  5,  6]],
                                                                            #
                                                                            #       [[ 7,  8,  9],
                                                                            #        [10, 11, 12]]])]

#---[ Searching Arrays ]------------------------------------------------------------------------------------------------------------------------------

#You can search an array for a certain value and return the indices that contain the match.

#where() method

#Find indices where value is 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print(x)                                                                    #(array([3, 5, 6]),)

#Find indices where values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print(x)                                                                    #(array([1, 3, 5, 7]),)

#Find indices where values are odd
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)                                            

print(x)                                                                    #(array([0, 2, 4, 6]),)

#searchsorted() method - peforms a binary search in the array and returns the index where the specified value would be inserted to maintain the search order.
# - Assumed to be used on sorted arrays.

#Basic example
#The number 7 should be placed in index 2 to maintain the sort order.
arr = np.array([5, 6, 8, 9])
x = np.searchsorted(arr, 7)

print(x)                                                                    #2

#Right side
arr = np.array([5, 6, 8, 9])
x = np.searchsorted(arr, 7, side='right')

print(x)                                                                    #2

#Multiple values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])

print(x)                                                                    #[1 2 3]

#---[ Sorting Arrays ]--------------------------------------------------------------------------------------------------------------------------------

#sort() function

#Numeric order
arr = np.array([3, 2, 0, 1])
x = np.sort(arr)

print(x)                                                                    #[0 1 2 3]

#Alphabetic order
arr = np.array(['banana', 'cherry', 'apple'])
x = np.sort(arr)

print(x)                                                                    #['apple' 'banana' 'cherry']

#Boolean order
arr = np.array([True, False, True])
x = np.sort(arr)

print(x)                                                                    #[False  True  True]

#2-D arrays
arr = np.array([[3, 2, 4], [5, 0, 1]])
x = np.sort(arr)

print(x)                                                                    #[[2 3 4]
                                                                            # [0 1 5]]

#---[ Filtering Arrays ]------------------------------------------------------------------------------------------------------------------------------

#In NumPy, you can filter an array using a boolean index list (list of booleans corresponding to indices in the array).
# - If the value at an index is True, that element is contained in the filtered array.
# - If the value at an index is False, that element is excluded from the filtered array.

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

print(newarr)                                                               #[41 43]

#Creating the filter array for numbers greater than 42
arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)                                                       #[False, False, True, True]
print(newarr)                                                           #[43 44]

#Creating the filter array for even elements
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)                                                       #[False, True, False, True, False, True, False]
print(newarr)                                                           #[2 4 6]

#Creating the filter directory from the array of values greater than 42
arr = np.array([41, 42, 43, 44])
filter_arr = (arr > 42)
newarr = arr[filter_arr]

print(filter_arr)                                                       #[False False True True]
print(newarr)                                                           #[43 44]

#Creating the filter directory from the array of even elements
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = (arr % 2 == 0)
newarr = arr[filter_arr]

print(filter_arr)                                                       #[False  True False  True False  True False]
print(newarr)                                                           #[2, 4, 6]