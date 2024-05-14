# Traces are a common syntax used to apply higher order functions as part of executing a def statement
# def trace(fn):
#     def wrapped(x):
#         print("This decorator add this print statement to any function")
#         return fn(x)
#     return wrapped


#Explinations 
# 1. The name "trace" is bound in the global enviorment to a function which accepts formal parameter <fn> 
# 2. The name "wrapped" is bound locally inside trace to a function which accepts formal parameter <x>
# 3. When trace is called on a function it applies  the wrapper to the function

# that @ symbol can be used as a way to apply decorators to a function



