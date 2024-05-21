# Tree Recursion: Is a Tree-shaped processes which arise whenever executing thhe body of a recursive funtion makes more than one call to itself.
#Fib tree recursion

def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped
 
@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Repition in Tree-Recursive Computation: Can be sped up by remembering the results of specific computations

    
