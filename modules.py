#!/usr/bin/python3

#What is a Module?
#Consider a module to be the same as a code library.
#It is a file containing a set of functions you want to include in your application.

#Create a Module
#To create a module, just save the code you want in a file with the file extension ".py".
#The code below has been saved as mymodule.py.
def greeting(name):
    print("Hello, " + name + "!")

#Use a Module
#The import statement allows you to use a module.
import mymodule

mymodule.greeting("Kaizen")                     #Hello, Kaizen!

#Variables in a Module
#The module can contain functions, but also varaibles of all types.
#The code below has bene saved in mymodule.py.
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

#Import the module named mymodule and access the person1 dictionary
import mymodule

a = mymodule.person1["country"]
print(a)                                        #Norway

#Naming a Module
#Modules can have any name, but mus have the ".py" file extension.

#Renaming a Module
#You can create an alias when you import a module, by using the as keyword:
import mymodule as mx

a = mx.person1["country"]
print(a)                                        #Norway

#Built-in Modules
#There are several built-in modules in Python which can be imported as needed.
import platform

x = platform.system()
print(x)                                        #Linux

#Using the dir() Function
#There is a built-in function named dir() that lists all the function names (or variable names) within a module.
import platform

x = dir(platform)
print(x)                                        #['_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', 
                                                #'__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', 
                                                #'_default_architecture', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', 
                                                #'_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version', '_platform', '_platform_cache', 
                                                #'_pypy_sys_version_parser', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', 
                                                #'_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'java_ver', 'libc_ver', 
                                                #'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 
                                                #'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 
                                                #'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']

#Import From Module
#You can choose to import only parts from a module by using the keyword from.
"""
When importing using the from keyword, do not use the module name when referring to elements in the module:
 - GOOD:    person1["country"]
 - BAD:     mymodule.person1["country"]
"""
from mymodule import person1

print(person1["country"])                       #Norway