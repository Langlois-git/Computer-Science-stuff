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
from operator import add

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

# Consider the following implementations of count_fives and count_primes which use the sum_digits and is_prime functions from earlier assignments:

def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.
    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

# The implementations look quite similar! Generalize this logic by writing a function count_cond, which takes in a two-argument predicate function condition(n, i). count_cond returns a one-argument function that takes in n, which counts all the numbers from 1 to n that satisfy condition when called.

# Note: When we say condition is a predicate function, we mean that it is a function that will return True or False.

def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def counter(n):
        condition_is_true = 0
        current_value = 1
        while current_value <= n:
            if condition(n, current_value):
                condition_is_true += 1
            current_value += 1
        return condition_is_true
    return counter
 

run_docstring_examples(count_cond, globals(), True)
# Write a function that takes in two numbers and returns the smallest number that is a multiple of both.

def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    add_small_value = min(a, b)
    add_big_value = max(a, b)
    big_total = add_big_value
    small_total = add_small_value
    
    while (big_total % small_total != 0) and small_total <= 100:
        if small_total > big_total:
            big_total += add_big_value 
        else:
            small_total += add_small_value
    return small_total 

run_docstring_examples(multiple, globals(), True)
