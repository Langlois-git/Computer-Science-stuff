#Q1: Num Eights
# Write a recursive function num_eights that takes a positive integer n and returns the number of times the digit 8 appears in n

from doctest import run_docstring_examples

def num_eights(n):
    """Returns the number of times 8 appears as a digit of n
    
    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(8782089)
    3
    """
    def is_eight(n):
        return n == 8
    def last_digit(n):
        return n % 10
    
    if is_eight(n):
        return 1
    elif n < 10:
        return 0
    else:
        return is_eight(last_digit(n)) + num_eights(n//10)

run_docstring_examples(num_eights, globals(), True)

#Q2: Digit Distance:
# For a given integer, the digit distance is the sum of the absolute differances between consecutive digits. For example the digit distance of 6 is 0. the digit distance of 61 is 5, the digit distance of 13451 is ( 2 + 1 + 1 +4) = 8

def digit_distance(n):
    """Determines the digit distance of n

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    """
    def last_digit(n):
        return n % 10
    def second_last_digit(n):
        return ((n % 100) - (n % 10)) // 10
    
    if n < 10:
        return 0
    else:
        return abs(last_digit(n) - second_last_digit(n)) + digit_distance(n//10)

run_docstring_examples(digit_distance, globals(), True)

#Q3: Interleaved sum
# Write a function interleaved_sum which takes in a number n and two one-argument functions: odd_func and even_func. It applies odd_func to every off number and even_func to every even number from 1 to n (including n) and returns the sum
#Implement this function without using any loops or directly testing if a number is odd or even. (no modulos % allowed) instead of checking if a number is odd or even, start with one, which we know is odd

def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ...+ -> n

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1 + 2*2 + 3 + 4 * 4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2 + 3*3 + 4 + 5 * 5
    41
    >>> interleaved_sum(4, triple, square) # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple) # 1*1 + 2*3 + 3*3 + 4*3
    28
    """
    def is_even(n):
        if n == 0:
            return True
        else:
            return is_odd(n-1)
    
    def is_odd(n):
        if n == 0:
            return False
        else:
            return is_even(n-1)
    
    if n < 0:
        return 0
        
    elif is_even(n):
        return even_func(n) + interleaved_sum(n-1, odd_func, even_func)
        
    elif is_odd(n):
        return odd_func(n) + interleaved_sum(n-1, odd_func, even_func)
        
run_docstring_examples(interleaved_sum, globals(), True)

#Q4 

def next_larger_coin(coin):
    """Return the next largest coin
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Returns None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Return the next smaller coin
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    next_smaller_coin(2) # Returns None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Returns the number of ways to make change using the standard US coin set
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100)
    242
    >>> count_coins(200)
    1463
    """
    if total == 0:
        return 1
    elif total < 0:
        return 0
    else:
        return 
    
