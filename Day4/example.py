# we're disussing about module and functions in Python
# calendar module in Python provides functions related to calendar operations
import calendar as c
print(c.month(2024,3))
print(c.month(1947, 8))
print(c.calendar(2024))

import math as c
print(c.pow(2,3))
print(c.pow(2,-1))

print(c.factorial(5))

# module is not containing only functions name but aslo containing data members and also containing classes 
print(c.pi)  # pi is a data member inside math module

# can we see function inside the module?
print(dir(c))  # dir() function shows all the functions available inside a module

# There is function called help() in Python which provides the documentation of the module or function
print(help(c.sqrt))  # documentation of sqrt function inside math module



# Math module in Python provides various mathematical functions and constants
# Functions in python are defined using the def keyword
# Syntax of function:  
# def function_name(parameters):
#     """docstring"""       
#     function_body
#     return statement

# acos(x, /)	Return the arc cosine of x, in radians.
# The result is between 0 and pi.
# acosh(x, /)	Return the inverse hyperbolic cosine of x.
# asin(x, /)	Return the arc sine of x, in radians.

print(c.pi)
print(c.e)