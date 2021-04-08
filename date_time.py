#!/usr/bin/python3

#Python Date
#A date in Python is a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()

print(x)                                        #2020-10-23 15:45:16.672558

#Return the date parts name of weekday
import datetime

x = datetime.datetime.now()

print(x.year)                                   #2020
print(x.month)                                  #10
print(x.day)                                    #23    
print(x.hour)                                   #15
print(x.minute)                                 #45
print(x.second)                                 #16
print(x.microsecond)                            #672558
print(x.strftime("%A"))                         #Friday

#Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)                                        #2020-05-17 00:00:00

#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.
#It takes one parameter (format) to specify the format of the returned string.
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B %d, %Y"))                  #June 01, 2018

"""
Directive   Description                                                     Example
---------   -----------------------------------------------------------     ------------------------   
%a 	    Weekday, short version 	                                    Wed 	
%A 	    Weekday, full version 	                                    Wednesday 	
%w 	    Weekday as a number 0-6, 0 is Sunday 	                    3 	
%d 	    Day of month 01-31 	                                            31 	
%b 	    Month name, short version 	                                    Dec 	
%B 	    Month name, full version 	                                    December 	
%m 	    Month as a number 01-12 	                                    12 	
%y 	    Year, short version, without century 	                    18 	
%Y 	    Year, full version 	                                            2018 	
%H 	    Hour 00-23 	                                                    17 	
%I 	    Hour 00-12 	                                                    05 	
%p 	    AM/PM 	                                                    PM 	
%M 	    Minute 00-59 	                                            41 	
%S 	    Second 00-59 	                                            08 	
%f 	    Microsecond 000000-999999 	                                    548513 	
%z 	    UTC offset 	                                                    +0100 	
%Z 	    Timezone 	                                                    CST 	
%j 	    Day number of year 001-366 	                                    365 	
%U 	    Week number of year, Sunday as the first day of week, 00-53     52 	
%W 	    Week number of year, Monday as the first day of week, 00-53     52 	
%c 	    Local version of date and time 	                            Mon Dec 31 17:41:00 2018 	
%x 	    Local version of date 	                                    12/31/18 	
%X 	    Local version of time 	                                    17:41:00 	
%% 	    A % character 	                                            %
"""

#The strptime() Method
#The datetime object has a method for formatting strings which represent dates/times into datetime objects.
#It takes two parameters: string representing a date/time and format code.
import datetime

datetime_string = '4/8/2021 3:21:48 PM'
datetime_object = datetime.datetime.strptime(datetime_string, '%m/%d/%Y %I:%M:%S %p')

print(datetime_object.strftime('%m/%d/%Y %H:%M'))			#04/08/2021 15:21
