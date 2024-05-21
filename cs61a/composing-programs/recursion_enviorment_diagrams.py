def fact(n):
    """This function utilizes recursion to calulate factorial of n"""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Recursive functions have the same lexical as their initial call (usually globaL)

# Iteration vs recursion
# - Recusion simplifies the amount of variable
