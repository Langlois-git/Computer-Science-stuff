# This file will act as my own reffernce in understanding functions acting as arguments (higher order function), consider the following funtcions that all calculate a summation of numbers up to "n"

def sum_naturals(n):
    total = 0
    k = 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    total = 0
    k = 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total = 0
    k = 1
    while k <= n:
        total, k = total + 8/((4*k-3) * (4*k-1)), k + 1
    return total

# It is clear that these functions differ only in name and the function of k computed to be added, so there is an underlying pattern. Patterns can be expressed as functions. our funciton will look something like the following 

def summation(n, term):
    total = 0
    k = 1
    while k <= n:
        total, k = total + term(k), k + 1
    return k

def cube(x):
    return x*x*x

def sum_cubes_2(n):
    return summation(n, cube)

def identity(x):
    return x

def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

    
    

