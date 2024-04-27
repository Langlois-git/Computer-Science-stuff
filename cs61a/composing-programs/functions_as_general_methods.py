# It can be seen that some functions descibe a method or algorithim of computation, consider the following:  which implements a general method for iterative improvement and uses it to compute the golden ratio. The golden ratio, often called "phi", is a number near 1.6 that appears frequently in nature, art, and architecture. An iterative improvement algorithm begins with a guess of a solution to an equation. It repeatedly applies an update function to improve that guess, and applies a close comparison to check whether the current guess is "close enough" to be considered correct.

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

# The improve function is a general method of repetitive refinement, it doesnt specify what is bejing solved.
# The golden ration can be calculated by repeatedly summing the inverse of any positive number with one and that it is 1 less than its square
# We can express these properties as functions, to be used with our impove function

def phi_update(guess):
    return 1/ guess + 1

def square_close(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y): < tolerance

