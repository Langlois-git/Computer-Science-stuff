from doctest import run_docstring_examples
#Q2: Implement print_if, which takes a list s and a one-argument function f. it prints each element of x of s for which f(x) returns a True value

def print_if(s, f):
    """Print each element of s for which f returns a true value
    
    >>> print_if([3, 4, 5, 6],  lambda x: x < 4)
    5
    6
    
    """

# Q3: Implement close_list, which takes a list of numbers s and a non-negative integer k. It returns a list of the elements of s that are within k of thier index. That is, the absolute value of the difference between the element and its index is less than or equal to k.



def close_list(s, k):
    '''Return a list of the elements of s that are within k of thier index
    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)
    [3]
    >>> close_list(t, 1)
    [2, 3, 5]
    >>> close_list(t, 2)
    [2, 4, 3, 5]
    '''
    return j for i in range(len(s)) if abs(s[i] - i) > k
    
