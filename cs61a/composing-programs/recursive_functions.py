# A recursive function is a function that calls itself either directly or indirectly
# If a number a is divisible by nine then is digit sum is also divisible by nine.
# Digit sums are useful for typo detection like on credit card numbers the last digit is a checksum digit that is computed from all the other digits
# Credit cards use the luhn algorithim for thier check sum

"""Summing digits without using a while statement"""

def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last_digit, last_digit = split(n)

    x = sum_digits(all_but_last_digit) + last_digit
    print(x)
    return x

# Anatomy of a Recursive function.
# - The def statement header is similar to other functions
# - Then usually a conditional statement follows that checks for base cases
# - Base cases are evaluated without recursive calls (computed directly)
# - Recursive cases are evaluated without recursive calls
    
    
