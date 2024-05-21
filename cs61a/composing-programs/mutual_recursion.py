# The Luhn Algorithim (used by credit cards)
# 1. From the right most digit,(The check digit), moving left, double the value of every second digit; if the product of the doubling operation is larger than 9 (ex 7*2=14) Then sum digits of the products (ex 2 * 7 = 14, 1 + 4 = 5)
# 2. Take the sum of all the digits
# A valid credit card number will always have a luhn sum that is a multiple of 10

def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# Mutual recursion: When to functions call each other
