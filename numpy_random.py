#!/usr/bin/python3

#Random Numbers in NumPy
"""
Random number does not mean a different number every time; random means something that cannot be predicted logically.
Random numbers generated through a generation algorithm are called pseudo random.
True random numbers can be generated using an outside source (kestrokes, mouse movements, network data, etc.).
We don't need truly random numbers unless it is related to security (encryption keys) or the basis of an application is randomness (digital roulette wheels).
This tutorial will use pseudo random numbers.
"""

#Data Distribution
"""
Data distribution is a list of all possible values and how often each value occurs.
These types of lists are important when working with statistics and data science.
The random module offers methods that return randomly generated data distributions.
"""

#---[ Random Intro ]----------------------------------------------------------------------------------------------------------------------------------

from numpy import random

#Generate Random Integer
x = random.randint(100)
print(x)                                                                    #47                                

#Generate Random Float
x = random.rand()
print(x)                                                                    #0.8890083471203096

#Generate Random Array

#The randint() method takes a size parameter where you can specify the shape of an array.
x = random.randint(100, size=(5))
print(x)                                                                    #[69 35 69 85 20]

x = random.randint(100, size=(3,5))
print(x)                                                                    #[[27  6 17 48 37]
                                                                            # [27 65 83 70 33]
                                                                            # [87 57  4 22 44]]

#The rand() method also allows you to specify the shape of an array.
x = random.rand(5)
print(x)                                                                    #[0.59089795 0.58231483 0.88775679 0.87807438 0.50498678]

x = random.rand(3, 5)
print(x)                                                                    #[[0.53973604 0.09972401 0.85190124 0.71945863 0.51131637]
                                                                            # [0.67589076 0.73709258 0.92641797 0.0368256  0.54740297]
                                                                            # [0.06562039 0.83339419 0.79547536 0.01968309 0.61071111]]
#Generate Random Number from Array

#The choice() method allows you to generate a random value based on an array of values.
# - It takes an array as a parameter and randomly returns one of the values.
x = random.choice([3, 5, 7, 9])
print(x)                                                                    #5

#The choice() method also allows you to return an array of values.
# - Add a size parameter to specify the shape of the array.
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)                                                                    #[[9 9 9 9 5]
                                                                            # [9 3 3 7 5]
                                                                            # [5 7 3 5 5]]

#---[ Random Data Distribution ]----------------------------------------------------------------------------------------------------------------------

"""
A random distribution is a set of random numbers that follow a certain probability density function.
 - Problem Density Function - A function that describes a continuous probability (i.e. probability of all values in an array).
We can generate random numbers based on defined probabilities using the choice() method of the random module.
 - The choice() method allows us to specify the probability of each value.
 - The probability is set by a number between 0 (never) and 1 (always).
 _ The sum of all probabilities should be 1.
"""

from numpy import random

#Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7, or 9.
# - The probability of the value to be 3 is 0.1
# - The probability of the value to be 5 is 0.3
# - The probability of the value to be 7 is 0.6
# - The probability of the value to be 9 is 0.0
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)                                                                    #[7 7 7 7 7 7 7 5 5 7 5 5 7 7 7 7 5 7 7 5 5 5 5 7 7 3 7 7 7 7 7 7 7 7 7 7 7
                                                                            # 7 5 5 7 7 7 7 7 7 7 7 7 5 5 7 7 5 7 7 7 7 5 7 7 7 5 7 7 7 7 7 3 7 5 5 7 7
                                                                            # 5 5 7 7 3 3 7 5 5 5 3 5 7 5 7 5 3 7 7 7 5 7 5 3 7 7]

#You can return arrays of any shape and size by specifying the shape in the size parameter.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)                                                                    #[[5 7 7 7 7]
                                                                            # [3 7 3 5 7]
                                                                            # [7 5 7 7 3]]

#---[ Random Permutations ]---------------------------------------------------------------------------------------------------------------------------

"""
A random permutation refers to an arrangement of elements such as [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
The NumPy Random modules provides 2 methods for this:
  (1) shuffle()
  (2) permutation()
"""

from numpy import random
import numpy as np

#Shuffling Arrays
#Shuffle means changing the arrangement of elements in-place within the array, itself, and returns the shuffled, original array.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)

print(arr)                                                                  #[1 5 4 3 2]

#Generating Permutations of Arrays
#This method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])
newarr = random.permutation(arr)

print(newarr)                                                               #[3 5 1 2 4]

#---[ Seaborn Module ]--------------------------------------------------------------------------------------------------------------------------------

"""
Seaborn is a library that uses Matplotlib underneath to plot graphs.
It can be used to visualize random distributions.
"""

#Install Seaborn
#Seaborn can be installed using the command: pip install seaborn
# $ python -m pip install seaborn
# Collecting seaborn
#   Downloading seaborn-0.11.0-py3-none-any.whl (283 kB)
#      |████████████████████████████████| 283 kB 1.3 MB/s 
# Collecting scipy>=1.0
#   Downloading scipy-1.5.4-cp38-cp38-manylinux1_x86_64.whl (25.8 MB)
#      |████████████████████████████████| 25.8 MB 172 kB/s 
# Requirement already satisfied: numpy>=1.15 in /home/dgrewal/.local/lib/python3.8/site-packages (from seaborn) (1.19.4)
# Requirement already satisfied: pandas>=0.23 in /home/dgrewal/.local/lib/python3.8/site-packages (from seaborn) (1.1.4)
# Collecting matplotlib>=2.2
#   Downloading matplotlib-3.3.3-cp38-cp38-manylinux1_x86_64.whl (11.6 MB)
#      |████████████████████████████████| 11.6 MB 69 kB/s 
# Requirement already satisfied: python-dateutil>=2.7.3 in /home/dgrewal/.local/lib/python3.8/site-packages (from pandas>=0.23->seaborn) (2.8.1)
# Requirement already satisfied: pytz>=2017.2 in /home/dgrewal/.local/lib/python3.8/site-packages (from pandas>=0.23->seaborn) (2020.4)
# Collecting kiwisolver>=1.0.1
#   Downloading kiwisolver-1.3.1-cp38-cp38-manylinux1_x86_64.whl (1.2 MB)
#      |████████████████████████████████| 1.2 MB 12.6 MB/s 
# Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3
#   Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
#      |████████████████████████████████| 67 kB 329 kB/s 
# Collecting pillow>=6.2.0
#   Downloading Pillow-8.0.1-cp38-cp38-manylinux1_x86_64.whl (2.2 MB)
#      |████████████████████████████████| 2.2 MB 5.3 MB/s 
# Collecting cycler>=0.10
#   Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
# Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7.3->pandas>=0.23->seaborn) (1.14.0)
# Installing collected packages: scipy, kiwisolver, pyparsing, pillow, cycler, matplotlib, seaborn
# Successfully installed cycler-0.10.0 kiwisolver-1.3.1 matplotlib-3.3.3 pillow-8.0.1 pyparsing-2.4.7 scipy-1.5.4 seaborn-0.11.0

import matplotlib.pyplot as plt
import seaborn as sns

#Plotting a Displot
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

#Plotting a Displot without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

#---[ Normal Distribution ]---------------------------------------------------------------------------------------------------------------------------

"""
A Normal Distribution is also referred to as a "Gaussian Distribution" after German mathematician Carl Friedrich Gauss.
It is one of the most important distributions since it fits the probability distribution of many events (IQ Scores, Hearbeat, etc.).
Use the random.normal() method to get a Normal Data Distribution.
The random.normal() method has 3 parameters:
  (1) loc      Where the peak of the bell exists (mean).
  (2) scale    How flat the graph distribution should be (standard deviation).
  (3) size     Shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Generate a random normal distribution of size 2 x 3
x = random.normal(size=(2,3))
print(x)                                                                    #[[ 1.06638216 -0.61432603 -2.2029733 ]
                                                                            # [ 1.65494846 -0.10238858  0.37005667]]

#Generate a random normal distribution of size 2 x 3 with a mean at 1 and standard deviation of 2.
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)                                                                    #[[ 2.47500699  2.16933776  3.04773648]
                                                                            # [-2.50831805 -2.56450312  2.89696494]]

#Visualization of Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

#---[ Binomial Distribution ]-------------------------------------------------------------------------------------------------------------------------

"""
A Binomial Distribution is a discrete distribution that is defined as a separate set of events, whereas each result is discrete.
It describes the outcome of binary scenarios (coin toss).
It has 3 parameters.
  (1) n        Number of trials
  (2) p        Probability of occurence of each trial (for coin toss it is 0.5 each)
  (3) shape    The shape of the returned array
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Given 10 trials for coin toss, generate 10 data points.
x = random.binomial(n=10, p=0.5, size=10)
print(x)                                                                    #[3 4 3 7 6 7 6 6 6 5]

#Visualization of Binomial Distribution
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

#Difference Between Normal Distribution and Binomial Distribution
# - The main difference is that Normal Distribution is continuous whereas a Binomial Distribution is discrete.
# - If there are enough data points, Normal Distribution is similar to Binomial Distribution with certain loc and scale.
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

#---[ Poisson Distribution ]--------------------------------------------------------------------------------------------------------------------------

"""
The Poisson Distribution is another discrete distribution.
It estimates how many times an event can happen in a specified amount of time (Someone who normally eats twice daily eating thrice daily).
It has 2 parameters:
  (1) lam     Rate or known number of occurrences (eating twice daily = 2).
  (2) size    The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Generate a random 1x10 distribution for occurence 2
x = random.poisson(lam=2, size=10)
print(x)                                                                    #[2 3 1 3 3 2 4 1 0 0]

#Visualization of Poisson Distribution
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#Difference Between Normal Distribution and Poisson Distribution
# - The main difference is that Normal Distribution is continuous whereas a Poisson Distribution is discrete.
# - again, if there are large enough Poisson Distribution, it will become similar to a Normal Distribution with certain std dev, and mean.
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show() 

#Difference Between Poisson Distribution and Binomial Distribution
# - The difference is very subtle: Binomial Distribution is for discrete trials, whereas Poisson Distribution is for continuous trials.
# - For very large n and near-zero p, Binomial Distribution is near identical to Poisson Distribution such that n * p is nearly equal to lam.
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show() 

#---[ Uniform Distribution ]--------------------------------------------------------------------------------------------------------------------------

"""
In a Uniform Distribution is used to describe probability where every event has an equal chance of occurring (generation of random numbers)/
It has 3 parameters:
  (1) a       Lower-bound (default 0.0).
  (2) b       Upper-bound (default 1.0).
  (3) size    The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Generate a 2x3 Uniform Distribution
x = random.uniform(size=(2, 3))
print(x)                                                                    #[[0.99334983 0.72417514 0.18401795]
                                                                            # [0.62094619 0.84128046 0.65286049]]

#Visualization of Uniform Distribution
sns.distplot(random.uniform(size=1000), hist=False)
plt.show() 

#---[ Logistic Distribution ]-------------------------------------------------------------------------------------------------------------------------

"""
A Logistic Distribution is used to describe growth.
It is used extensively in machine learning in logistic regression, neural networks, etc.
It has 3 parameters:
  (1) loc      Where the peak is - mean (default 0).
  (2) scale    The flatness of distribution - standard deviation (default 1).
  (3) size     The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw 2x3 samples from a logistic distribution with mean at 1 and standard deviation of 2.0.
x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)                                                                    #[[1.38295002 1.32856967 6.46333548]
                                                                            # [0.27819345 3.71383209 3.12953539]]
#Visualization of Logistic Distribution
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

#Difference Between Logistic Distribution and Normal Distrbution
# - Both distributions are nearly identical, but a logistic distribution has more area under the tails
# - The Logistic Distribution represents more possibility of occurrence of events further away from the mean.
# - For higher value of scale (standard deviation), the Normal and Logistic distributions are near identical apart from the peak.
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()

#---[ Multinomial Distribution ]----------------------------------------------------------------------------------------------------------------------

"""
Multinomial Distribution is a generalization of a Binomial Distribution.
It describes outcomes of multi-nomial scenarios, unlike binomial where scenarios must be only 1 of 2 (blood type of population, dice roll outcome).
It has 3 parameters:
  (1) n        Number of possible outcomes (6 for a dice roll).
  (2) pvals    List of probabilities of outcomes (for a dice roll: [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
  (3) size     The shape of the returned array.
"""

from numpy import random

#Draw out a sample for dice roll
# - Multinomial samples will NOT produce a single value; they will produce 1 value for each pval.
# - They are a generalization of binomial distribution 
#    + Their visual representation and similarity of normal distribution is the same as that of multiple Binomial Distributions.
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)                                                                    #[3 0 0 0 3 0]

#---[ Exponential Distribution ]----------------------------------------------------------------------------------------------------------------------

"""
Exponential Distribution is used for describing time until next event (failure, success, etc.).
It has 2 parameters:
  (1) scale    Inverse of rate - see lam in Poisson Distribution (default 1.0).
  (2) size     The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw out a sample for exponential distribution with 2.0 scale and 23x size.
x = random.exponential(scale=2, size=(2, 3))
print(x)                                                                    #[[0.53243082 0.55915908 0.37184984]
                                                                            # [0.58041191 0.0400673  0.44781221]]

#Visualization of Exponential Distribution
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

#Relation Between Poisson Distribution and Exponential Distribution
# - Poisson Distribution deals with number of occurrences or an event in a time period.
# - Exponential Distribution deals with the time between these events.

#---[ Chi Square Distribution ]-----------------------------------------------------------------------------------------------------------------------

"""
Chi Square Distributionis used as a basis to verify the hypothesis.
It has 2 parameters:
  (1) df      Degree of freedom.
  (2) size    The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw out a sample for Chi Squared Distribution with degree of freedom of 2 and size of 2x3.
x = random.chisquare(df=2, size=(2,3))
print(x)                                                                    #[[2.85738448 1.28099029 2.89376304]
                                                                            # [1.22461892 3.12091151 1.40834177]]

#Visualization of Chi Square Distribution
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

#---[ Rayleigh Distribution ]-------------------------------------------------------------------------------------------------------------------------

"""
Rayleigh Distribution is used in signal processing.
It has 2 parameters:
  (1) scale    Decides how flat the distribution will be - standard deviation (default 1.0).
  (2) size     The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw out a sample for Rayleigh Distribution with scale of 2 and size of 2x3.
x = random.rayleigh(scale=2, size=(2,3))
print(x)                                                                    #[[2.65682876 2.16858634 5.0490129 ]
                                                                            # [2.22168305 4.05696949 1.25257441]]

#Visualization of Rayleigh Distribution
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

#Similarity Between Rayleigh Distribution and Chi Square Distribution
# - At unit standard deviation the and 2 degrees of freedom, rayleigh and chi square represent the same distributions.

#---[ Pareto Distribution ]---------------------------------------------------------------------------------------------------------------------------

"""
The Pareto Distribution follows Pareto's law (80-20 distribution where 20% of the factors cause 80% of the outcome).
It has 2 parameters:
  (1) a       Shape parameter
  (2) size    The shape of the returned array.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw out a sample for Pareto Distribution with shape of 2 and size 2x3
x = random.pareto(a=2, size=(2,3))
print(x)                                                                    #[[0.13448729 0.74773998 0.21334766]
                                                                            # [0.04154645 0.01357176 1.41335777]

#Visualization of Pareto Distribution
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show() 

#---[ Zipf Distribution ]-----------------------------------------------------------------------------------------------------------------------------

"""
Zipf Distributions are used to sample data based on Zipf's Law.
Zipf's Law: In a collection, the nth common term is 1/n times of the most common term (5th common word in English occurs nearly 1/5th times as of the most).
It has 2 parameters:
  (1) a       Distribution parameter
  (2) size    The shape of the returned array. 
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Draw out a sample for Zipf Distribution with distribution parameter of 2 and size of 2x3.
x = random.zipf(a=2, size=(2, 3))
print(x)                                                                    #[[1 2 4]
                                                                            # [2 1 1]]

#Visualization of Zipf Distribution
# - Sample 1000 points but plotting only ones with value < 10 for a more meaninhful chart.
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show() 