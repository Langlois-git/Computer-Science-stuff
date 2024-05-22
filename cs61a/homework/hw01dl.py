from doctest import run_docstring_examples

# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if n > 1:
        for i in range(n-1, 0, -1):
            if n % i == 0:
                return i
    else:
        print("The paramater must be an integer > 1")

run_docstring_examples(largest_factor, globals(), True)

# Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.
#
# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.
# The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.
#
# This sequence of values of n is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    steps = 1
    print(n)
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = n // 2
            print(n)
        elif n % 2 != 0:
            n = (n*3)+1
            print(n)
    return steps

run_docstring_examples(hailstone, globals(), True)

#Q4 Count coins
# Given a positive integer total a set of coins makes change for total if the sume of the values of coins is total. Here we will use standard us coin values 1, 5, 10, 25 for example the following sets make change for 15,
# 5 1-cents and 1 1-cents
# 3 5-cent coins 
# 5 1-cents and 2 5-cents
# 1 10-cent and 1 5-cent 

#Therefore there are 6 ways to make change for 15
# Write a recursive function count_couins that takes a positive integer total and returns the number of ways to make change for total coins

# You can use either of the following functions 

def next_larger_coin(coin): 
    """Returns the next larger coin in order
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways used to make change with the standard US coin set"""
