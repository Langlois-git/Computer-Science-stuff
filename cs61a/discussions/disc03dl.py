#Q1 Swipe: Implement swipe, which prints the digits of argument n, one per line, first bacward, then forward. The left most digit is printed only once. Do not use a while or for or string. (use recursion 

from doctest import run_docstring_examples

def swipe(n):
    """Prints the digits of n, forward then backward
    
    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n//10)
        print(n % 10)

run_docstring_examples(swipe, globals(), True)

# Q2 Skip Factorial: Define the base case for a skip_factorial function, which returns the product of every other integer starting from n

def skip_factorial(n):
    """Returns the product of every other integer starting from n

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 1
    384
    """
    if n < 1:
        return 1
    else:
        return n * skip_factorial(n-2)
        
run_docstring_examples(skip_factorial, globals(), True)

#Q3 Is_prime: Implement is_prime, that takes an integer n > 1. It returns True if n is prime

def is_prime(n):
    """Returns True if n is prime
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def iterator(n):
        if n < 2:
            return 1
        else:
            return iterator(n - 1) 
    if n % iterator(n) == 0:
        return  False
    return iterator(n)
        
