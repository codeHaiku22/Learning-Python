#!/usr/bin/python3

#RegEx Module
#Python has a built-n package called re which can ebe used to work with regular expressions.

#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes, we have a match.")                                              #Yes, we have a match.
else:
    print("No, we don not have a match.")

#RegEx Functions
#The re module offers a set of functions that allows us to search a string for a match.
"""
Function    Description
----------  -----------------------------------------------------------------
findall 	Returns a list containing all matches
search 	    Returns a Match object if there is a match anywhere in the string
split 	    Returns a list where the string has been split at each match
sub 	    Replaces one or many matches with a string
"""    

#Metacharacters
#Metacharacters are characters with a special meaning.
"""
Character 	Description 	                                                            Example
----------  --------------------------------------------------------------------------  -------
[] 	        A set of characters 	                                                    "[a-m]" 	
\ 	        Signals a special sequence (can also be used to escape special characters) 	"\d" 	
. 	        Any character (except newline character) 	                                "he..o" 	
^ 	        Starts with 	                                                            "^hello" 	
$ 	        Ends with 	                                                                "world$" 	
* 	        Zero or more occurrences 	                                                "aix*" 	
+ 	        One or more occurrences 	                                                "aix+" 	
{} 	        Exactly the specified number of occurrences 	                            "al{2}" 	
| 	        Either or 	                                                                "falls|stays" 	
() 	        Capture and group
"""

#Special Sequences
#A special sequence is a \ followed by one of the characters in the list below and has a special meaning.
"""
Character 	Description 	                                                                                                    Example
----------  ------------------------------------------------------------------------------------------------------------------  ---------
\A 	        Returns a match if the specified characters are at the beginning of the string 	                                    "\AThe" 	
\b 	        Returns a match where the specified characters are at the beginning or at the end of a word                         r"\bain"
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")                        r"ain\b" 	
\B 	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word      r"\Bain"
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")                        r"ain\B" 	
\d 	        Returns a match where the string contains digits (numbers from 0-9) 	                                            "\d" 	
\D 	        Returns a match where the string DOES NOT contain digits 	                                                        "\D" 	
\s 	        Returns a match where the string contains a white space character 	                                                "\s" 	
\S 	        Returns a match where the string DOES NOT contain a white space character 	                                        "\S" 	
\w 	        Returns a match where the string contains any word characters                                                       "\w"    
            (characters from a to Z, digits from 0-9, and the underscore _ character) 	 	
\W 	        Returns a match where the string DOES NOT contain any word characters 	                                            "\W" 	
\Z 	        Returns a match if the specified characters are at the end of the string 	                                        "Spain\Z"
"""

#Sets
#A set is a set of characters inside a pair of square brackets [] with a special meaning.
"""
Set 	    Description
----------  ---------------------------------------------------------------------------------------------------------------------
[arn] 	    Returns a match where one of the specified characters (a, r, or n) are present 	
[a-n] 	    Returns a match for any lower case character, alphabetically between a and n 	
[^arn] 	    Returns a match for any character EXCEPT a, r, and n 	
[0123] 	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
[0-9] 	    Returns a match for any digit between 0 and 9 	
[0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59 	
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
[+] 	    In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

#The finall() Function
#Returns a list containing all matches
# - If no matches are found, an empty list is returned.
import re

txt = "The rain in Spain"

x = re.findall("ai", txt)
print(x)                                                                        #['ai', 'ai']

#The search() Function
#Searches the string for a match and returns a Match object if there is a match.
# - If there is more than 1 match, only the first occurrence of the match will be returned.
# - If no matches are found, the value None is returned.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white space character is locted in position",  x.start())     #The first white space character is locted in position 3

#The split() Function
#Returns a list where the string has been split at each match.
import re

txt = "The rain in Spain"
x = re.split("\s", txt)

print(x)                                                                        #['The', 'rain', 'in', 'Spain']

#Control the number of occurrences by specifying the maxsplit parameter
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)

print(x)                                                                        #['The', 'rain in Spain']

#The sub() Function
#Substitutes (replaces) the mathces with the text of your choice.
import re

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)

print(x)                                                                        #The-rain-in-Spain

#Control the number of substitutions by specifying the count parameter
import re

txt = "The rain in Spain"
x = re.sub("\s", "-", txt, 2)

print(x)                                                                        #The-rain-in Spain

#Match Object
#The Match object is an object that contains information about the search and the result.
# - If there is no match, the value None will be returned instead of the Match object.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)

print(x)                                                                        #<re.Match object; span=(5, 7), match='ai'>

#The Match object has properties and methods used to retrieve information about the search and the result:
# - .span() returns a tuple containing the start and end positions of the match
# - .string returns the string passed into the function
# - .group() returns the part of the string where there was a match

#Print the position (start and end) of the first match occurrence
# - The regular expression looks for any words that start with an upper case "S".
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())                                                                 #(12, 17)

#Print the string passed into the function
# - The regular expression looks for any words that start with an upper case "S".
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)                                                                 #The rain in Spain

#Print the part of the string where there was a match
# - The regular expression looks for any words that start with an upper case "S".
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())                                                                #Spain