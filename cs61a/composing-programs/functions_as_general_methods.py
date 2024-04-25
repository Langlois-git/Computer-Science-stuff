# It can be seen that some functions descibe a method or algorithim of computation, consider the following:  which implements a general method for iterative improvement and uses it to compute the golden ratio. The golden ratio, often called "phi", is a number near 1.6 that appears frequently in nature, art, and architecture. An iterative improvement algorithm begins with a guess of a solution to an equation. It repeatedly applies an update function to improve that guess, and applies a close comparison to check whether the current guess is "close enough" to be considered correct.

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


