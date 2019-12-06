"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f:
  print(f.read())
# IT WORKS - interesting not sure why we would need this. But curious.
# Do you bite your thumb at us, sir?
# I do bite my thumb, sir.
# Do you bite your thumb at us, sir?
# No, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.
# Do you quarrel, sir?
# Quarrel, sir? No, sir.

f.closed
print(f.closed)
# doesnt need closing :

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w') as f:
  f.write('this is a test')
#   print(f.read()) not sure how to test read isn't working 
# line 35, in <module>
#     print(f.read())
# io.UnsupportedOperation: not readable
# WAIT!! checked file that was created and this is a test is printed inside :)


f.closed
print(f.closed)
