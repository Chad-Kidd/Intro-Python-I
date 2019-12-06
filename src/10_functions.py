# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        # note to self true and false NEED to be capitalized otherwise invalid

num = input("Enter a number: ")
num = int(num)
# Read a number from the keyboard
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if (num % 2) == 0:
  print("number" + " is even!")
else:
  print("number" + " is Odd!")

# works in pipenv woohoo!!