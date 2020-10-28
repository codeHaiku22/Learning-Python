#!/usr/bin/python3

#RegEx Module
#Python has a built-n package called re which can be used to work with regular expressions.

#RegEx Functions
#The re module offers a set of functions that allows us to search a string for a match.
"""
Function  Description
--------  -----------------------------------------------------------------
findall   Returns a list containing all matches
search 	  Returns a Match object if there is a match anywhere in the string
split 	  Returns a list where the string has been split at each match
sub 	  Replaces one or many matches with a string
match     Matches a pattern to a string.
"""    

#The findall() Function
#Returns a list containing all matches
# - If no matches are found, an empty list is returned.
#re.findall(<pattern>, <string>, [flags=0])
import re

txt = "The rain in Spain"

x = re.findall("ai", txt)
print(x)                                                                        #['ai', 'ai']

#The search() Function
#Searches the string for a match and returns a Match object if there is a match.
# - If there is more than 1 match, only the first occurrence of the match will be returned.
# - If no matches are found, the value None is returned.
#re.search(<pattern>, <string>, [flags=0])

#Search the string to see if it starts with "The" and ends with "Spain":
import re
re.sub
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes, we have a match.")                                              #Yes, we have a match.
else:
    print("No, we don not have a match.")


#Search the string and return the first whitespace (\s) character.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white space character is locted in position",  x.start())     #The first white space character is locted in position 3

#The split() Function
#Returns a list where the string has been split at each match.
#re.split(<pattern>, <string>, (occurences=0), [flags=0])
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
#Substitutes (replaces) the matches with the text of your choice.
#re.sub(<pattern>, <replacement>, <string>, [max=0])
import re

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)

print(x)                                                                        #The-rain-in-Spain

#Control the number of substitutions by specifying the count parameter
import re

txt = "The rain in Spain"
x = re.sub("\s", "-", txt, 2)

print(x)                                                                        #The-rain-in Spain

#The match() Function
#Matches a regular express pattern to a string.
# - If matches are found, the match object ois returned.
# - If no matches are found, the value None is returned.
#re.match(<pattern>, <string>, [flags=0])
import re

line = "Cats are smarter than dogs."

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group(0):", matchObj.group(0))                             #matchObj.group(0): Cats are smarter than dogs.
    print("matchObj.group(1):", matchObj.group(1))                             #matchObj.group(1): Cats
    print("matchObj.group(2):", matchObj.group(2))                             #matchObj.group(2): smarter
else:
   print("No match!!")    

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

#Regular Expression Examples

#Metacharacters
#Metacharacters are characters with a special meaning.
"""
Character  Description 	                                                               Example
---------  --------------------------------------------------------------------------  -------------
[] 	       A set of characters 	                                                       "[a-m]" 	
\ 	       Signals a special sequence (can also be used to escape special characters)  "\d" 	
. 	       Any character (except newline character) 	                               "he..o" 	
^ 	       Starts with 	                                                               "^hello" 	
$ 	       Ends with 	                                                               "world$" 	
* 	       Zero or more occurrences 	                                               "aix*" 	
+ 	       One or more occurrences 	                                                   "aix+" 	
{} 	       Exactly the specified number of occurrences 	                               "al{2}" 	
| 	       Either or 	                                                               "falls|stays" 	
() 	       Capture and group
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

#Regular Expression Modifiers: Option Flags
#Flags are optional and can be used to control various aspects of matching.
#You can provide multiple modifiers using exclusive OR (|).
"""
Flag  Description
----  ----------------------------------------------------------------------------------------------------------------------------------------------------------------
re.I  Performs case-insensitive matching.
re.L  Interprets words according to the current locale; affects the alphabetic group (\w and \W) and the word boundary behavior (\b and \B).
re.M  Makes $match the end of a line (not just the beginning of a string) and makes ^ match the start of any line (not just the start of the string).
re.S  Makes a period (dot) match any character, including a new line.
re.U  Interprets letters according to the Unicode character set; affects the alphabetic group (\w and \W) and the word boundary behavior (\b and \B).
re.X  Permits the "cuter" regular expression syntax; ignores whitespace (except inside a set [] or when escaped by a backslash); treats unescaped # as comment marker.
"""

#More Complex Regular Expressions
#You don't have to match on fixed string alone.  You can match on just about anything with more complex regular expressions.
"""
Expression   Description
-----------  ----------------------------------------------------------------------------------------------------------------------
^            Matches beginning of line
$            Matches end of line
.            Matches any singler character except newline (using m option allows it to match newline)
[...]        Matches any single character in brackets
[^...]       Matches any single character not in brackets
re*          Matches 0 or more occurrences of preceding expression
re+          Matches 1 or more occurrents of preceding expression
re?          Matches 0 or 1 occurrence of preceding expression
re{n}        Matches exactly n number of occurrences in preceding expression
re{n,}       Matches n or more occurrences of preceding expression
re{n,m}      Matches at least n and at most m occurrences of preceding expression
a|b          Matches either a or b
(re)         Groups regular expressions and remembers matched text
(?imx)       Temporarily toggles on i, m, or x options within a regular expression (if in parantheses, only that area is affected)
(?-imx)      Temporarily toggles off i, m, or x options within a regular expression (if in parantheses, only that area is affected)
(?: re)      Groups regular expressions without remembering matched text.
(?imx: re)   Temporarily togges on i, m, or x options within parentheses.
(?-imx: re)  Temporarily togges off i, m, or x options within parentheses.
(?#...)      Comment
(?= re)      Specifies position using a pattern (does not have a range).
(?! re)      Specifies position using pattern negation (does not have a range).
(?> re)      Matches independent pattern without backtracking.
\w           Matches word characters
\W           Matches non-word characters
\s           Matches whitespace (equivalent to [\t\n\r\f])
\S           Matches non-whitespace
\d           Matches digits (equivalent to [0-9])
\D           Matches non-digits
\A           Matches beginning of string
\Z           Matches end of string (if newline exists, matches just before newline)
\z           Matches end of string
\G           Matches power where last match finished
\b           Matches word boundaries when outside brackets (matches backspace (0x08) when inside brackets)
\B           Matches non-word boundaries
\n,\t,etc.   Matches newlines, carriage returns, tabs, etc.
\1...\9      Matches nth grouped subexpression
\10          Matches nth grouped subexpression if it already matched (otherwise refers to the octal representation of a character code)
[aeiou]      Matches a single character in the given set
[^aeiou]     Matches a single character outside the given set
"""

#Literal Characters
"""
Characters  Description
----------  --------------
Python      Match "Python"
"""

#Character Classes
"""
Class        Description
-----------  ----------------------------------------------------------------------------------
[Pp]ython    Matches "Python" or "python"
rub[ye]      Matches "ruby" or "rube"
[aeiou]      Matches any one lowercase vowel
[0-9]        Matches any digit; same as [0123456789]
[a-z]        Matches any lowercase ASCII character
[A-Z]        Matches any uppercase ASCII character
[a-zA-Z0-9]  Matches any lowercase ASCII character, any uppercase ASCII character, or any digit   
[^aeiou]     Matches anything other than a lowercase vowel
[^0-9]       Matches anything other than a digit
"""

#Special Character Classes
"""
Class  Description
-----  -------------------------------------------------
.      Matches any character except newline
\d     Matches a digit: [0-9]
\D     Matches a nondigit: [^0-9]
\s     Matches a whitespace character: [\t\r\n\f]
\S     Matches a nonwhitespace character: [^\t\r\n\f]
\w     Matches a single word character: [A-Za-z0-9_] 
\W     Matches a single nonword character: [^A-Za-z0-9_]
"""

#Repetition Cases
"""
Class    Description
-------  -------------------------------------------
ruby?    Matches "rub" or "ruby" - the y is optional
ruby*    Matches "rub" plus 0 or more y's
ruby+    Matches "rub" plus 1 or more y's
\d{3}    Matches exactly 3 digits
\d{3,}   Matches 3 or more digits
\d{3,5}  Matches 3, 4, or 5 digits    
"""

#Greedy and Nongreedy Repetition
"""
Repition  Description
--------  -----------------------------------------------------------
<.*>      Greedy repetition: matches "<python>perl>"
<.*?>     Nongreedy repetition: matches "<python>" in "<python>perl>"   
"""

#Grouping with Parantheses
"""
Grouping          Description
----------------  ------------------------------------------------
\D\d+             Non-grouped: + repeats \d
(\D\d)+           Grouped: + repeats \D\d pair
([Pp]ython(,)?)+  Matches "Python", "Python, python, python", etc.
"""

#Backreferences
"""
Backreference       Description
------------------  --------------------------------------------------------------------------------------------------------------------------
([Pp])ython&\1ails  Matches python&pails or Python&Pails
(['"])[^\1]*\1      Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.
"""

#Alternatives
"""
Alternative    Description
-------------  -------------------------------------------
python|perl    Matches "python" or "perl"
rub(y|le)      Matches "ruby" or "ruble"
Python(!+|\?)  "Python" followed by one or more ! or one ?
"""

#Anchors
"""
Anchor       Description
-----------  --------------------------------------------------------------------------
^Python      Matches "Python" at the start of a string or line
Python$      Matches "Python" at the end of a string or line
\APython     Matches "Python" at the start of a string
Python\Z     Matches "Python" at the end of a string 
\bPython\b   Matches "Python" at a word boundary
\brub\B      \B is a nonword boundary: match "rub" in "rube" and "ruby", but not alone
Python(?=!)  Matches "Python" if followed by an "!" exclamation point
Python(?!!)  Matches "Python" if not followed by an "!" exclamation point
"""

#Special Syntax with Parentheses
"""
Syntax        Description
------------  --------------------------------------------
R(?#comment)  Matches "R"; all the rest is a comment
R(?i)uby      Case-insensitive while matching "uby"
R(?i:uby)     Case-insensitive while matching "uby"
rub(?:y|le))  Group only without creating \1 backreference
"""