# Using newtons method to compute square roots
# How to compute a square root
# 1, iteratively refine a guess x about the square root of a using the following update formula
# x = (x+(a/x))/2 <- bablonian method

def square_root(a):
    x = 1 # This is our guess
    while x * x != a: # <- while our guess is not the square_root of a
        x = square_root_update(x, a) # <- update our guess using the bablonian method
    return x #<- Return our guess (which is now the square_root of a)

def square_root_update(x, a): #<- <x> is our guess, <a> is the parameter we are square rooting 
    return (x + (a/x))/2 #<- bablonian method

#Problem, when computing irrational number, such as square_root(2), our program runs forever so we have to develop a tolerance
# Special Case: Cube Roots (iteratively refine a guess x about the cube root of a)
# x = (x*2+(a/x^2))/3 <- bablonian method

def cube_root(a):
    x = 1
    while x * x * x != a:
        x = cube_root_update(x, a)
    return x

def cube_root_update(x, a):
    return ((x*2) + a/(x*x))/3

# Our cube root function suffers the same problem, we can fix both of these problems at once by generalizng thier computation and fixing it within the generalization

def iterative_improve(update, close, guess = 1):
    while not close(guess): # While our guess != what we want it too, update it
        guess = update(guess)
    return guess

# In order to solve our problem of irrational numbers, we can create a fucntion that checks if they approximately equal what we want.

def approx_equal(x, y, tolerance=0.0001): #<- 10 ^ -15
    return abs(x - y) < tolerance #Tells us if the two values <x> and <y> are approximately equal

# Now we can rewrite our previous functions using our iterative_improve general method

def square_root_improved(a):
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_equal(x*x, a)
    return iterative_improve(update, close)

# For cube root we can do the same thing, but we will provide lambda expressions for the update and close functions

def cube_root_improved(a):
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_equal(x*x*x, a))

#note that tolerances dont work for every value, to circumvent this we can alter our tolerane, or we could change our implementation of improve so that we have a maximum number of iterations.
 
def iterative_improve_alpha(update, close, guess = 1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
    return guess


