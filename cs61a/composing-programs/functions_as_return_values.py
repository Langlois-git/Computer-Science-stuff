"""Generalizations"""

def make_addition_function(n):
    """Return a function that takes one argument <k>, and return K + N
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def addition_function(k):
        return k + n
    return addition_function
   
# Functions as return values
# Functions defined within other function bodies are bound to names in a local frame.

# If we were to call make_adder(1)(2)
# 1. It would return our addition function which add n and K, in this case n = 1 so our addition function is "add_one"
# 2. next it would supply add_one the argument 2, so add_one(2) = 3, therefore make_adder(1)(2) = 3

#The purpose of Higher-Order functions
# - Functions are first-class, meaning the can be manipulated as values in pyhton, they can be supplied as arguments and returned as values
# A Higher-Order function is a function that takes a function as an argument or returns a function as a return value
# Higher=order functions are useful because they can express general mehods of computation, they remove repition from programs, they seperate concerns among functions allowing each function to have exactly one job.


