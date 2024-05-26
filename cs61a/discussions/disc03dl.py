from doctest import run_docstring_examples

#Q3: Is Prime
"""Implement is_prime that takes an integer n greater than 1. It returns True if n is a prime number and False otherwise. Try following the approach below, but implement it recursively without using a while (or for) statement."""

def is_prime_loop(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

"""You will need to define another "helper" function (a function that exists just to help implement this one). Does it matter whether you define it within is_prime or as a separate function in the global frame? Try to define it to take as few arguments as possible."""

def is_prime(n):
    """Returns True if n is prime
    >>> is_prime(8)
    False
    >>> is_prime(7)
    True
    >>> is_prime(2)
    True
    """
    def is_prime_i(i):
        if n == i:
            return True
        elif n % i == 0:
            return False
        else:
            return is_prime_i(i + 1)
    return is_prime_i(2)

run_docstring_examples(is_prime, globals(), True)


