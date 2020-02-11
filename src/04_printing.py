"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("%d %f %s" % (x,y,z)) # 10 2.245520 I like turtles!
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers 

# Use the 'format' string method to print the same thing
print(f'{x} {y} "{z}"'.format(x, y, z)) #10, 2.24552, "I like turtles!"

# Finally, print the same thing using an f-string
print(f"{x} {y} {z}") #10 2.24552 I like turtles!