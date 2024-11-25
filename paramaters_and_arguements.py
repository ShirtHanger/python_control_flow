from defining_and_calling_functions import *

""" Working ahead, but basically you can import functions for file readibility """

print_banner()

# banner_text is the parameter

def print_banner_and_text(banner_text):
    print("=======================")
    print(f'{banner_text}')
    print("=======================")
    
# 'Wololo!' is the arguement

print_banner_and_text('Wololo!')
""" Prints:
=======================
'Wololo!'
=======================
"""

"""
Accepting a varying number of arguments
-----------------------------------------
In JS, you can accept any number of parameters like this
const sum = (...nums) => {
  total = 0;

  nums.forEach((num) => {
    total += num;
  });

  return total;
};


console.log(sum(1, 5, 10));
// prints: 16
-----------------------------------------
In Python, you can do it like this
"""

def sum(*args):
    print(type(args))
    # prints: <class 'tuple'>
    total = 0
    
    for arg in args:
        total += arg

    return total

print(sum(1, 5, 10))
# prints: 16
# 'args' can be anything, but using args is convention.

# Anything after the * will follow this format

def sum(greeting, *args):
    print(greeting)
    # prints: Hello, friend
    total = 0
    
    for arg in args:
        total += arg

    return total

print(sum("Hello, friend", 1, 5, 10))
# Hello, friend
# 16

