# Q2 Make Keeper

# Implement make_keeper, which takes a positive integer n and returns a function f that takes as its argument another one-argument function cond. When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true value when called on each of those integers. Each integer is printed on a separate line."""
from doctest import run_docstring_examples

def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    def f(cond):
        i = 1
        while i <= n:
            if cond(i) == True:
                print(i)
            i += 1
    return f

run_docstring_examples(make_keeper, globals(), True)

#Q3 Digit_finder

"""Implement find_digit, which takes in a positive integer k and returns a function that takes in a positive integer x and returns the kth digit from the right of x. If x has fewer than k digits, it returns 0.

For example, in the number 4567, 7 is the 1st digit from the right, 6 is the 2nd digit from the right, and the 5th digit from the right is 0 (since there are only 4 digits).

Important: You may not use strings or indexing for this problem.

Use floor dividing by a power of 10 gets rid of the rightmost digits"""


def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    def f(x):
        modulo_divisor = 1 * (10**k)
        floor_divisor = modulo_divisor // 10
        x_minus_left_digits = x % modulo_divisor
        kth_digit_of_x = x_minus_left_digits // floor_divisor
        return kth_digit_of_x
    return f

run_docstring_examples(find_digit, globals(), True)

# Q4: Match Maker
"""Implement match_k, which takes in an integer k and returns a function that takes in a variable x and returns True if all the digits in x that are k apart are the same.

For example, match_k(2) returns a one argument function that takes in x and checks if digits that are 2 away in x are the same.

match_k(2)(1010) has the value of x = 1010 and digits 1, 0, 1, 0 going from left to right. 1 == 1 and 0 == 0, so the match_k(2)(1010) results in True.

match_k(2)(2010) has the value of x = 2010 and digits 2, 0, 1, 0 going from left to right. 2 != 1 and 0 == 0, so the match_k(2)(2010) results in False.

Important: You may not use strings or indexing for this problem.

Floor dividing by powers of 10 gets rid of the rightmost digits"""

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        pattern_to_find = 1 * (10**k)
        while x // (10 ** k) > 0:
            if find_digit(1)(x) != find_digit(k+1)(x):
                return False
            x //= 10
        return True
    return check

run_docstring_examples(match_k, globals(), True)
