# print(True and 13) # <- This should evaluate to true because non-zero integers evaluate to true in python
# print(False or 0) # <- This should evaluate to False because 0 is false in python
# print(not 10) # <- This should evaluate to False because non-zero integers are True, not True = False
# print(not None)# <- In python the None type evaluates to false so not False would equal True
# print(True and 1/0) # <- This should return a DIVIDEBYZERO Error because 
# print(True or 1/0) #<- This should return True. Because the lhs is True, short circuting or
# print(-1 and 1 > 0) #<- This should return True
# print(-1 or 5) #<- This should return True
# print(2 and 1) #<- This should return True 

from doctest import run_docstring_examples

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    def fog_equals_gof(x):
        return f(g(x)) == g(f(x))
    return fog_equals_gof

run_docstring_examples(composite_identity, globals(), True)
