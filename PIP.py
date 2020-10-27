#!/usr/bin/python3

#What is PIP?
#PIP is a package manager for Python packages.

#What is a Package?
#A package contains all of the files you need for a module.
#Modules are Python code libraries you can include in your project.

#Check if PIP is Installed:
"""
$ pip --version
"""

#If pip is not in the PATH:
"""
$ python3 -m pip --version
"""

#Install PIP
#Visit https://pypi.org/project/pip/
#For Linux specific: https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers
"""
Arch:
$ sudo pacman -S python-pip

Debian/Ubuntu:
$ sudo apt install python3-venv python3-pip

Fedora:
$ sudo dnf install python3 python3-wheel

openSUSE:
$ sudo zypper install python3-pip python3-setuptools python3-wheel
"""

#Download a Package
#Navigate to the location of Python's script directory and enter the following command.
"""
$ python3 -m pip install camelcase
"""

#Using a Package
import camelcase

c = camelcase.CamelCase()

txt = "hello, world!"

print(c.hump(txt))                              #Hello World!

#Find Packages
#Find more packages at https://pypi.org/.

#Remove a Package
"""
$ python3 -m pip uninstall camelcase
"""

#List Installed Packages
"""
$ python3 -m pip list
"""