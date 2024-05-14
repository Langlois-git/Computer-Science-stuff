#Function currying - a way of manipulating function

from operator import add

def make_addition_function(n):
    """This function preforms addition and can be used to create addition functions

    >>> make_addition_function(2)(3)
    5
    >>> add_two = make_addition_function(2)
    >>> add_two(3)
    5
    """
    return lambda k: n + k

def curry2(f): # 2 is there so we remmber the function we have created takes to arguments
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g 

# Currying is transforming a multi-argument function into a sing-argument, higher-order function that returns the function that takes the rest of the arguement


