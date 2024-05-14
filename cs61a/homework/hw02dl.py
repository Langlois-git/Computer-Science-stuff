from doctest import run_docstring_examples
from functions import identity, square, increment, triple
from operator import add, mul

# run_docstring_examples(function, globals(), True)

"""Write a function called product that returns the product of the first n terms of a sequence. Specifically, product takes in an integer n and term, a single-argument function that determines a sequence. (That is, term(i) gives the ith term of the sequence.) product(n, term) should return term(1) * ... * term(n)""" 

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    total = 1
    k = 1
    while k <= n:
        total = total * term(k) 
        k += 1
    return total
        
run_docstring_examples(product, globals(), True)

"""Let's take a look at how product is an instance of a more general function called accumulate, which we would like to implement"""

def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    total = start
    k = 1
    while k <= n:
        total = fuse(total, term(k))
        k += 1
    return total

run_docstring_examples(accumulate, globals(), True)

# Then, implement summation (from lecture) and product as one-line calls to accumulate.
def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)
run_docstring_examples(summation_using_accumulate, globals(), True)

def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)
run_docstring_examples(product_using_accumulate, globals(), True)

"""Implement the function make_repeater that takes a one-argument function f and a positive integer n. It returns a one-argument function, where make_repeater(f, n)(x) returns the value of f(f(...f(x)...)) in which f is applied n times to x. For example, make_repeater(square, 3)(5) squares 5 three times and returns 390625, just like square(square(square(5)))"""

def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    def repeater(x):
        for i in range(n):
            x = f(x)
        return x 
    return repeater

run_docstring_examples(make_repeater, globals(), True)
