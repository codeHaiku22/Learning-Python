#!/usr/bin/python3

#Pandas
"""
Pandas is a library that is used for working with data sets.
It was created in 2008 by Wes McKinney and has functions for analyzing, cleaning, exploring, and manipulating data.
Pandas has references to "Panel Data" and "Python Data Analysis".
Pandas is good for analyzing big data and making conclusions based on statistical theories.
Pandas can clean messy data sets and make them readable and relevant.
Pandas also can provide answers to questions such as:
 - Is ther ea correlation between 2 or more columns?
 - What is the average value?
 - What is the maximum value?
 - What is the minimum value?
"""

#---[ Install Pandas ]---------------------------------------------------------------------------------------------------------------------------------

#Pandas can be installed using the command: pip install pandas
#python -m pip install pandas
#Collecting pandas
#  Downloading pandas-1.1.5-cp38-cp38-manylinux1_x86_64.whl (9.3 MB)
#     |████████████████████████████████| 9.3 MB 8.7 MB/s
#Requirement already satisfied: numpy>=1.15.4 in /home/dgrewal/.local/lib/python3.8/site-packages (from pandas) (1.19.4)
#Requirement already satisfied: python-dateutil>=2.7.3 in /home/dgrewal/.local/lib/python3.8/site-packages (from pandas) (2.8.1)
#Requirement already satisfied: pytz>=2017.2 in /home/dgrewal/.local/lib/python3.8/site-packages (from pandas) (2020.4)
#Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7.3->pandas) (1.14.0)
#Installing collected packages: pandas
#Successfully installed pandas-1.1.5

import pandas as pd

#Check pandas version
print(pd.__version__)                                                       #1.1.5

#Basic example
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

var = pd.DataFrame(mydataset)

print(var)                                                                  #    cars  passings
                                                                            #0    BMW         3
                                                                            #1  Volvo         7
                                                                            #2   Ford         2

#---[ Pandas Series ]---------------------------------------------------------------------------------------------------------------------------------

#A Panda Series is similar to a column in a table: it is a 1-dimensional array holding data of any type.

import pandas as pd

#Create a Pandas Series from a list
a = [1, 7, 2]
var = pd.Series(a)

print(var)                                                                  #0    1
                                                                            #1    7
                                                                            #2    2
                                                                            #dtype: int64

#Labels

#If nothing else is specified, the values are labeled with their index number (base 0).
# - This label can be used to access a specific value.
a = [1, 7, 2]
var = pd.Series(a)

print(var[0])                                                               #1

#With the index argument, you can name your own labels.
a = [1, 7, 2]
var = pd.Series(a, index = ["x", "y", "x"])

print(var)                                                                  #x    1
                                                                            #y    7
                                                                            #x    2
                                                                            #dtype: int64

#With labels, you can access an item by referring to the label.
a = [1, 7, 2]
var = pd.Series(a, index = ["x", "y", "x"])

print(var["y"])                                                             #7

#Key/Value Objects as Series

#You can also use a key/value object (dictionary) when creating a Pandas Series.
# - The keys of the dictionary become the labels.
calories = {"day1": 420, "day2": 380, "day3": 390}
var = pd.Series(calories)

print(var)                                                                  #day1    420
                                                                            #day2    380
                                                                            #day3    390
                                                                            #dtype: int64

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Pandas Series.
calories = {"day1": 420, "day2": 380, "day3": 390}
var = pd.Series(calories, index = ["day1", "day2"])

print(var)                                                                  #day1    420
                                                                            #day2    380
                                                                            #dtype: int64

#---[ Pandas DataFrames ]-----------------------------------------------------------------------------------------------------------------------------

#DataFrames
#Data sets in Pandas are usually multi-dimensional tables called DataFrames.
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
#If a Pandas Series is like a column, then a Pandas DataFrame is the whole table.

import pandas as pd

#Create a Pandas DataFrame from 2 Pandas Series
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

print(df)                                                                   #   calories  duration
                                                                            #0       420        50
                                                                            #1       380        40
                                                                            #2       390        45

#Locate Row
#Pandas uses the loc attribute to return 1 or more specified row(s).

#This example returns a Pandas Series.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

print(df.loc[0])                                                            #calories    420
                                                                            #duration     50
                                                                            #Name: 0, dtype: int64

#When using [], the result is a Pandas DataFrame.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

print(df.loc[[0,1]])                                                        #   calories  duration
                                                                            #0       420        50
                                                                            #1       380        40

#Named Indexes
#With the index argument, you can name your own indexes.

#Add a list of names to give each row a name.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)                                                                   #      calories  duration
                                                                            #day1       420        50
                                                                            #day2       380        40
                                                                            #day3       390        45

#Locate Named Indexes
#Use the named index in the loc attribute to return the specified row(s).

#Return "day2"
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df.loc["day2"])                                                       #calories    380
                                                                            #duration     40
                                                                            #Name: day2, dtype: int64

#---[ Pandas Read CSV ]-------------------------------------------------------------------------------------------------------------------------------

#A simple way to store big data sets is to use CSV files.
#If your data sets are stored in a CSV file, Pandas can load them into a Pandas DataFrame.

import pandas as pd

#Use to_string() to print the entire Pandas DataFrame
#wget https://www.w3schools.com/python/data.csv
df = pd.read_csv('data.csv')

print(df.to_string())                                                       #     Duration  Pulse  Maxpulse  Calories
                                                                            #0          60    110       130     409.1
                                                                            #1          60    117       145     479.0
                                                                            #2          60    103       135     340.0
                                                                            #...
                                                                            #168        75    125       150     330.4

#By default, when you print a Pandas DataFrame, you only get the first 5 rows and the last 5 rows:
df = pd.read_csv('data.csv')

print(df)                                                                   #     Duration  Pulse  Maxpulse  Calories
                                                                            #0          60    110       130     409.1
                                                                            #1          60    117       145     479.0
                                                                            #2          60    103       135     340.0
                                                                            #3          45    109       175     282.4
                                                                            #4          45    117       148     406.0
                                                                            #..        ...    ...       ...       ...
                                                                            #164        60    105       140     290.8
                                                                            #165        60    110       145     300.0
                                                                            #166        60    115       145     310.2
                                                                            #167        75    120       150     320.4
                                                                            #168        75    125       150     330.4

#---[ Pandas Read JSON ]------------------------------------------------------------------------------------------------------------------------------

#JSON = Python Dictionary
#JSON objects have the same format as Python dictionaries.
#Big data is also often stored or extracted as JSON.
#If your data sets are stored in a JSON file, Pandas can load them into a Pandas DataFrame.

import pandas as pd

#Use to_string() to print the entire Pandas DataFrame
#wget https://www.w3schools.com/python/data.js
df = pd.read_json('data.js')

print(df.to_string())                                                       #[169 rows x 4 columns]
                                                                            #     Duration  Pulse  Maxpulse  Calories
                                                                            #0          60    110       130     409.1
                                                                            #1          60    117       145     479.0
                                                                            #2          60    103       135     340.0
                                                                            #..
                                                                            #168        75    125       150     330.4         

#By default, when you print a Pandas DataFrame, you only get the first 5 rows and the last 5 rows:
df = pd.read_json('data.js')

print(df)                                                                   #     Duration  Pulse  Maxpulse  Calories
                                                                            #0          60    110       130     409.1
                                                                            #1          60    117       145     479.0
                                                                            #2          60    103       135     340.0
                                                                            #3          45    109       175     282.4
                                                                            #4          45    117       148     406.0
                                                                            #..        ...    ...       ...       ...
                                                                            #164        60    105       140     290.8
                                                                            #165        60    110       145     300.4
                                                                            #166        60    115       145     310.2
                                                                            #167        75    120       150     320.4
                                                                            #168        75    125       150     330.4
                                                                            #
                                                                            #[169 rows x 4 columns]

#Load a Python Dictionary into a Python DataFrame
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)

print(df)                                                                   #   Duration  Pulse  Maxpulse  Calories
                                                                            #0        60    110       130       409
                                                                            #1        60    117       145       479
                                                                            #2        60    103       135       340
                                                                            #3        45    109       175       282
                                                                            #4        45    117       148       406
                                                                            #5        60    102       127       300

#---[ Pandas Analyzing DataFrames ]-------------------------------------------------------------------------------------------------------------------

#Viewing the Data

import pandas as pd

#The head() Method
#One of the most used methods for getting a quick overview of a Pandas DataFrame is the head() method.
#The head() method returns the headers and a specified number of rows (default = 5), starting from the top.
df = pd.read_csv('data.csv')

print(df.head(3))                                                           #   Duration  Pulse  Maxpulse  Calories
                                                                            #0        60    110       130     409.1
                                                                            #1        60    117       145     479.0
                                                                            #2        60    103       135     340.0

#The tail() Method
#The tail() method allows us to view the last rows of the Pandas DataFrame.
#The tail() method returns theheaders and a specified number of rows (default = 5), starting from the bottom.
df = pd.read_csv('data.csv')

print(df.tail(3))                                                           #   Duration  Pulse  Maxpulse  Calories
                                                                            #166        60    115       145     310.2
                                                                            #167        75    120       150     320.4
                                                                            #168        75    125       150     330.4

#Getting Information About the Data

#The Pandas DataFrames object has a method called info() which provides information about the data set.
df = pd.read_csv('data.csv')

print(df.info())                                                          #<class 'pandas.core.frame.DataFrame'>
                                                                          #RangeIndex: 169 entries, 0 to 168
                                                                          #Data columns (total 4 columns):
                                                                          # #   Column    Non-Null Count  Dtype
                                                                          #---  ------    --------------  -----
                                                                          # 0   Duration  169 non-null    int64
                                                                          # 1   Pulse     169 non-null    int64
                                                                          # 2   Maxpulse  169 non-null    int64
                                                                          # 3   Calories  164 non-null    float64
                                                                          #dtypes: float64(1), int64(3)
                                                                          #memory usage: 5.4 KB
                                                                          #None

#---[ Pandas Cleaning Data ]--------------------------------------------------------------------------------------------------------------------------

#Pandas can be used to fix (clean) bad data withina data set.
#Bad data can be:
# - Empty cells
# - Data in the wrong format
# - Incorrect/wrong data
# - Duplicates

import pandas as pd
#wget https://www.w3schools.com/python/dirtydata.csv

#~~~[ Cleaning Empty Cells ]~~~~~~~~~~~~~~~~~~~~~

#Empty cells can potentially provide a wrong result when being analyzed.
#To remedy this you have 4 options:
# (1) remove the rows
# (2) replace all empty values
# (3) replace all empty values for a column
# (4) replace all empty values using mean, median, or mode

#The data set used in this section contains the following issues:

#Empty cells ("Date" in row 22, and "Calories" in rows 18 and 28).
"""
    Duration          Date  Pulse  Maxpulse  Calories
...
18        45  '2020/12/18'     90       112       NaN
...
22        45           NaN    100       119     282.0
...
28        60  '2020/12/28'    103       132       NaN
...
"""

#Remove Rows

#One way to deal with empty cells is to remove the rows that contain the empty cells.
# - In large data sets, this may not have too much impact on the analysis and results.

#Return a Pandas DataFrame with no empty cells
#The dropna() method returns a new Pandas DataFrame and will not change the original.
df = pd.read_csv('dirtydata.csv')
new_df = df.dropna()

print(new_df.to_string())                                                   #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.0
                                                                            #19        60  '2020/12/19'    103       123     323.0
                                                                            #20        45  '2020/12/20'     97       125     243.0
                                                                            #21        60  '2020/12/21'    108       131     364.2
                                                                            #23        60  '2020/12/23'    130       101     300.0                                                                            
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.0
                                                                            #29        60  '2020/12/29'    100       132     280.0  
                                                                            #30        60  '2020/12/30'    102       129     380.3                                                                            #                                                                           
                                                                            #31        60  '2020/12/31'     92       115     243.0

#If you want to change the original Pandas DataFrame, use the inplace = True argument.
# - A new Pandas DataFrame won't be returned, rather all rows containing NULL values are removed from the original.
df = pd.read_csv('dirtydata.csv')
df.dropna(inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.0
                                                                            #19        60  '2020/12/19'    103       123     323.0
                                                                            #20        45  '2020/12/20'     97       125     243.0
                                                                            #21        60  '2020/12/21'    108       131     364.2
                                                                            #23        60  '2020/12/23'    130       101     300.0                                                                            
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.0
                                                                            #29        60  '2020/12/29'    100       132     280.0  
                                                                            #30        60  '2020/12/30'    102       129     380.3                                                                            #                                                                           
                                                                            #31        60  '2020/12/31'     92       115     243.0

#Replace Empty Values

#Another way of dealing with empty cells is to insert a new value.
# - This prevents the deletion of the row entirely.

#Replace NULL values with the number 130
df = pd.read_csv('dirtydata.csv')
df.fillna(130, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.0
                                                                            #18        45  '2020/12/18'     90       112     130.0 <
                                                                            #19        60  '2020/12/19'    103       123     323.0
                                                                            #20        45  '2020/12/20'     97       125     243.0
                                                                            #21        60  '2020/12/21'    108       131     364.2
                                                                            #22        45           130    100       119     282.0 <
                                                                            #23        60  '2020/12/23'    130       101     300.0                                                                            
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.0
                                                                            #28        60  '2020/12/28'    103       132     130.0 <
                                                                            #29        60  '2020/12/29'    100       132     280.0  
                                                                            #30        60  '2020/12/30'    102       129     380.3                                                                            #                                                                           
                                                                            #31        60  '2020/12/31'     92       115     243.0

#Replace Only for a Specified Column
# - To only replace empty values for one column, specify the column name for the Pandas DataFrame.
df = pd.read_csv('dirtydata.csv')
df["Calories"].fillna(130, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.0
                                                                            #18        45  '2020/12/18'     90       112     130.0 <
                                                                            #19        60  '2020/12/19'    103       123     323.0
                                                                            #20        45  '2020/12/20'     97       125     243.0
                                                                            #21        60  '2020/12/21'    108       131     364.2
                                                                            #22        45           NaN    100       119     282.0
                                                                            #23        60  '2020/12/23'    130       101     300.0
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.0
                                                                            #28        60  '2020/12/28'    103       132     130.0 <
                                                                            #29        60  '2020/12/29'    100       132     280.0
                                                                            #30        60  '2020/12/30'    102       129     380.3
                                                                            #31        60  '2020/12/31'     92       115     243.0

#Replace Using Mean, Median, or Mode
# - A common way to replace empty cells is to calculate the mean, median, or mode value of the column.
# - Pandas uses the mean(), median(), and mode() methods to calculate the respective values for a specified column.

#mean()
df = pd.read_csv('dirtydata.csv')
df_mean = df["Calories"].mean()    #304.68
df["Calories"].fillna(df_mean, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.10
                                                                            #1         60  '2020/12/02'    117       145     479.00
                                                                            #2         60  '2020/12/03'    103       135     340.00
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.00
                                                                            #18        45  '2020/12/18'     90       112     304.68 <
                                                                            #19        60  '2020/12/19'    103       123     323.00
                                                                            #20        45  '2020/12/20'     97       125     243.00
                                                                            #21        60  '2020/12/21'    108       131     364.20
                                                                            #22        45           NaN    100       119     282.00
                                                                            #23        60  '2020/12/23'    130       101     300.00
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.00
                                                                            #28        60  '2020/12/28'    103       132     304.68 <
                                                                            #29        60  '2020/12/29'    100       132     280.00
                                                                            #30        60  '2020/12/30'    102       129     380.30
                                                                            #31        60  '2020/12/31'     92       115     243.00

#median()
df = pd.read_csv('dirtydata.csv')
df_median = df["Calories"].median()    #291.20
df["Calories"].fillna(df_median, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.10
                                                                            #1         60  '2020/12/02'    117       145     479.00
                                                                            #2         60  '2020/12/03'    103       135     340.00
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.00
                                                                            #18        45  '2020/12/18'     90       112     291.20 <
                                                                            #19        60  '2020/12/19'    103       123     323.00
                                                                            #20        45  '2020/12/20'     97       125     243.00
                                                                            #21        60  '2020/12/21'    108       131     364.20
                                                                            #22        45           NaN    100       119     282.00
                                                                            #23        60  '2020/12/23'    130       101     300.00
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.00
                                                                            #28        60  '2020/12/28'    103       132     291.20 <
                                                                            #29        60  '2020/12/29'    100       132     280.00
                                                                            #30        60  '2020/12/30'    102       129     380.30
                                                                            #31        60  '2020/12/31'     92       115     243.00

#mode()
df = pd.read_csv('dirtydata.csv')
df_mode = df["Calories"].mode()[0]    #300.00
df["Calories"].fillna(df_mode, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.10
                                                                            #1         60  '2020/12/02'    117       145     479.00
                                                                            #2         60  '2020/12/03'    103       135     340.00
                                                                            #...
                                                                            #17        60  '2020/12/17'    100       120     300.00
                                                                            #18        45  '2020/12/18'     90       112     300.00 <
                                                                            #19        60  '2020/12/19'    103       123     323.00
                                                                            #20        45  '2020/12/20'     97       125     243.00
                                                                            #21        60  '2020/12/21'    108       131     364.20
                                                                            #22        45           NaN    100       119     282.00
                                                                            #23        60  '2020/12/23'    130       101     300.00
                                                                            #...
                                                                            #27        60  '2020/12/27'     92       118     241.00
                                                                            #28        60  '2020/12/28'    103       132     300.00 <
                                                                            #29        60  '2020/12/29'    100       132     280.00
                                                                            #30        60  '2020/12/30'    102       129     380.30
                                                                            #31        60  '2020/12/31'     92       115     243.00

#~~~[ Cleaning Wrong Format ]~~~~~~~~~~~~~~~~~~~~~

#Cells with data of wrong format can make it difficult (sometimes impossible) to analyze data.
#To remedy this you have 2 options:
# (1) convert all cells in the columns to the same format
# (2) remove the rows

#The data set used in this section contains the following issues:

#Wrong format ("Date" in rows 22 and 26)
"""
    Duration          Date  Pulse  Maxpulse  Calories
...    
22        45           NaN    100       119     282.0    
...
26        60    2020/12/26    100       120     250.0
...
"""

#Convert Into a Correct Format

#We can use the Pandas to_datetime() method in this situation to make the convesion.
df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())                                                       #    Duration        Date  Pulse  Maxpulse  Calories
                                                                            #0         60  2020/12/01    110       130     409.1
                                                                            #1         60  2020/12/02    117       145     479.0
                                                                            #2         60  2020/12/03    103       135     340.0
                                                                            #...                                                    
                                                                            #22        45         NaT    100       119     282.0 <
                                                                            #23        60  2020-12-23    130       101     300.0
                                                                            #24        45  2020-12-24    105       132     246.0
                                                                            #25        60  2020-12-25    102       126     334.5
                                                                            #26        60  2020-12-26    100       120     250.0 <
                                                                            #27        60  2020-12-27     92       118     241.0
                                                                            #28        60  2020-12-28    103       132       NaN
                                                                            #29        60  2020-12-29    100       132     280.0
                                                                            #30        60  2020-12-30    102       129     380.3
                                                                            #31        60  2020-12-31     92       115     243.0

#Removing Rows

#Remove rows with a NULL value in the "Date" column
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())                                                       #    Duration        Date  Pulse  Maxpulse  Calories
                                                                            #0         60  2020/12/01    110       130     409.1
                                                                            #1         60  2020/12/02    117       145     479.0
                                                                            #2         60  2020/12/03    103       135     340.0
                                                                            #...                                                    
                                                                            #23        60  2020-12-23    130       101     300.0
                                                                            #24        45  2020-12-24    105       132     246.0
                                                                            #25        60  2020-12-25    102       126     334.5
                                                                            #26        60  2020-12-26    100       120     250.0
                                                                            #27        60  2020-12-27     92       118     241.0
                                                                            #28        60  2020-12-28    103       132       NaN
                                                                            #29        60  2020-12-29    100       132     280.0
                                                                            #30        60  2020-12-30    102       129     380.3
                                                                            #31        60  2020-12-31     92       115     243.0

#~~~[ Fixing Wrong Data ]~~~~~~~~~~~~~~~~~~~~~~~~~

#Incorrect/wrong data does not necessarily have to be empty cells or data that is in the wrong format.  It can just be wrong (199 instead of 1.99).
#To remedy this you have 2 options:
# (1) replace the incorrect/wrong values 
# (2) remove the rows

#The data set used in this section contains the following issues:

#Incorrect/wrong data ("Duration" in row 7)
"""
    Duration          Date  Pulse  Maxpulse  Calories
...
7        450  '2020/12/08'    104       134     253.3
...
"""

#Replace Values

#In this example, the duration value of 450 in row 7 should be 45.
df = pd.read_csv('dirtydata.csv')
df.loc[7, 'Duration'] = 45

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #3         45  '2020/12/04'    109       175     282.4
                                                                            #4         45  '2020/12/05'    117       148     406.0
                                                                            #5         60  '2020/12/06'    102       127     300.0
                                                                            #6         60  '2020/12/07'    110       136     374.0
                                                                            #7         45  '2020/12/08'    104       134     253.3 <
                                                                            #...
                                                                            #31        60  '2020/12/31'     92       115     243.0

#For small data sets the above remedy is feasible.
#For large data sets, rules can be created to make the replacements.
df = pd.read_csv('dirtydata.csv')

for x in df.index:
  if df.loc[x, 'Duration'] > 120:
    df.loc[x, 'Duration'] = 120

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #3         45  '2020/12/04'    109       175     282.4
                                                                            #4         45  '2020/12/05'    117       148     406.0
                                                                            #5         60  '2020/12/06'    102       127     300.0
                                                                            #6         60  '2020/12/07'    110       136     374.0
                                                                            #7        120  '2020/12/08'    104       134     253.3 <
                                                                            #...
                                                                            #31        60  '2020/12/31'     92       115     243.0


#Remove Rows

#Delete rows where Duration > 120.
df = pd.read_csv('dirtydata.csv')

for x in df.index:
  if df.loc[x, 'Duration'] > 120:
    df.drop(x, inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #3         45  '2020/12/04'    109       175     282.4
                                                                            #4         45  '2020/12/05'    117       148     406.0
                                                                            #5         60  '2020/12/06'    102       127     300.0
                                                                            #6         60  '2020/12/07'    110       136     374.0
                                                                            #8         30  '2020/12/09'    109       133     195.1
                                                                            #...
                                                                            #31        60  '2020/12/31'     92       115     243.0

#~~~[ Removing Duplicates ]~~~~~~~~~~~~~~~~~~~~~~~

#The data set used in this section contains the following issues:

#Duplicates (rows 11 and 12)
"""
    Duration          Date  Pulse  Maxpulse  Calories
...
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
...
"""  

#To discover duplicates, we can use the duplicated() method.
# - The duplicated() method rturns a Boolean value for each row.
df = pd.read_csv('dirtydata.csv')

print(df.duplicated())                                                      #0     False
                                                                            #1     False
                                                                            #2     False
                                                                            #...
                                                                            #11    False
                                                                            #12     True <
                                                                            #...
                                                                            #31    False
                                                                            #dtype: bool

#To remove duplicates, use the drop_duplicates() method.
df = pd.read_csv('dirtydata.csv')
df.drop_duplicates(inplace = True)

print(df.to_string())                                                       #    Duration          Date  Pulse  Maxpulse  Calories
                                                                            #0         60  '2020/12/01'    110       130     409.1
                                                                            #1         60  '2020/12/02'    117       145     479.0
                                                                            #2         60  '2020/12/03'    103       135     340.0
                                                                            #...
                                                                            #11        60  '2020/12/12'    100       120     250.7
                                                                            #13        60  '2020/12/13'    106       128     345.3                                                                            
                                                                            #...
                                                                            #31        60  '2020/12/31'     92       115     243.0

#---[ Pandas Data Correlations ]----------------------------------------------------------------------------------------------------------------------

import pandas as pd

#The corr() method is a powerful component of the Pandas module.
# - This method calculates the relationship (correlation) between each column within a data set.
# - The corr() method ignores colums that are not numeric.
df = pd.read_csv('data.csv')

print(df.corr())                                                            #          Duration     Pulse  Maxpulse  Calories
                                                                            #Duration  1.000000 -0.155408  0.009403  0.922717
                                                                            #Pulse    -0.155408  1.000000  0.786535  0.025121
                                                                            #Maxpulse  0.009403  0.786535  1.000000  0.203813
                                                                            #Calories  0.922717  0.025121  0.203813  1.000000

#Results Analyzed
#The result set of the corr() method is a table with numbers which repreent how well the relationship is between 2 columns.
# - This number is between -1 (inverse correlation) and 1 (perfect correlation).
#There are 3 general types of correlations.
# (1) Perfect Correlation   1, -1
# (2) Good Correlation      Between -1 and -0.6, Between 0.6 and 1
# (3) Bad Correlation       Between -0.6 and 0.6

#---[ Pandas Plotting ]-------------------------------------------------------------------------------------------------------------------------------

#Pandas uses the plot() method to create diagrams.
# - The kind argument can be used to specify the type of plotting desired.
#Python uses Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

import pandas as pd
import matplotlib.pyplot as plt

#Visualize the Pandas DataFrame
df = pd.read_csv('data.csv')
df.plot()

plt.show()

#Scatter Plot
#A scatter plot needs x and y axes.
# - Let's use Duration for the x axis and Calories for the y axis
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

#Histogram
#A histogram needs only one column.
# - Let's use the histogram to how the frequency of each interval: how many workouts lastered between 50 and 60 minutes
# - We will use the Duration column to create the histogram.
df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'hist')

plt.show()