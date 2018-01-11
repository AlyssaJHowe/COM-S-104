# Module containing a few examples of function definitions

# needed for the simple_postage function
from math import ceil

# Prints one verse of the song "99 bottles"
def sing_verse(num):
    print num, "bottles of beer on the wall"
    print num, "bottles of beer"
    print "If one of those bottles should happen to fall"
    print num - 1, "bottles of beer on the wall"

# Returns the area of a rectangle with given width and length
def area(width, length):
    result = width * length
    return result

# Prints the area of a rectangle with given width and length
def print_area(width, length):
    result = width * length
    print result

# Returns True if x is divisible by y
def is_divisible(x, y):
    return x % y == 0
    
# Prints encouragement for programming students
def encouraging_words(name):
    print "Good job,", name, "!"
    print "You've almost got it!"

# Returns the longest of two strings
def longest(first, second):
    if len(first) < len(second):
        answer = second
    else:
        answer = first
    return answer

#Returns the postage for a first-class letter up to 3.5 ounces
def simple_postage(weight):
    if weight <= 1.0:
        cost = .44
    else:
        cost = .44 + ceil(weight - 1) * .17
    return cost
