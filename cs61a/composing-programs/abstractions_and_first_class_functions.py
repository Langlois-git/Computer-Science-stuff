# The rights and privelages of first class functions are
# 1. They may be bound to names 
# 2. They may be passed as arguments to functions
# 3. They may be returned as the results of functions
# 4. They may be included in data structures
#
# In python Functions are awarded full first-class status

# What information needs to be passed on when using an abstraction?
# how many arguments are required by functions it utilizies
# the process upon which the function defines.

"""Chosing Names"""
# 1. Names should convey the meaning or purpose of the values to which they are bound
# 2. The type of value bound to the name is best documented in a functions docstring
# 3. Function names typically convey thier effect (print), thier behaviour (triple), or the claues returned (abs)

"""WHich values deserve a name?"""
# Repeated compound expressions:

if sqrt(square(a) + square(b)) > 1: 
    x = x + sqrt(square(a) + square(b)) # <- This expression is used twice, it is long and complicated so it would be better to describe it with a name

# Complex expressions

# n, k, i <- Usually integers 
# x, y, z <- Usually real numbers
# f, g, h <- Usually functions
