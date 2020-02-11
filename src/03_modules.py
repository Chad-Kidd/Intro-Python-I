"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(str(sys.argv)) #['03_modules.py']
print(len(sys.argv)) #1
# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform) #darwin
# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version) #3.7.5 (default, Nov  1 2019, 02:16:32)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
#GOOGLE IS YOUR FRIEND
# Print the current process ID
# YOUR CODE HERE
print(os.getpid()) #25594
# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd()) #/Users/ckidd/Documents/TLCS/Intro-Python-I/src
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin()) #root