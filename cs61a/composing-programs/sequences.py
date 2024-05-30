# A sequence is an ordered collection of values, they are a collection of behaviours shared among serveral different data types

# A sequence has a finite length, an empty sequence has a length of 0
# Elements can be selected from a sequence. The starting index of a sequence is 0

"Lists"
# len(list) will return the length of a list
# Lists can be added or multiplied by integers, these operations concatenate elements to the end of the original lists

example_list = [1, 2, 3, 4]
print(example_list * 2)

"List Comprehensions"
print([i+1 for i in example_list]) # will return a new list with operations aplied to each element


print([x for x in example_list if x % 2 == 0]) # This will return a new list with items only if they satisfy the condition

# The general for of a list Comprehension -> [<map expression> for <name> in <sequence expression> if <filter expression>]

"Agregation"
# A third common pattern in sequence processing is to aggregate all values in the sequence into a single value
# Such as max, sum and min

'Example'
# A perfect number is a number that is equal to the sum of its divisors
# The divisors of a number n are the numbers less than n that divide evenly into n

def list_divisors(n):
    return [x for x in range(1, n) if n % x == 0]

# using divsors we can compute all perfect numbers from 1 to n using list Comprehension

def perfect_numbers_to_n(n):
    return [1] + [x for x in range(1, n) if sum(list_divisors(x)) == x]

"Higher order funtions in List Comprehension"
# We can apply a function in a list to all elements using a List Comprehension

def apply_func(a_func, a_list):
    return [a_func(i) for i in a_list]

# Selecting only specific elements in a list can be expressed as a function utilizing List Comprehension

def filter_list(a_list, filter_func):
    return [x for x in a_list if filter_func(x) == True]

filter_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x % 2 == 0) # <- Will return all even values in the list

# Many forms of aggregation can be expressed as repeatedly applying to argument functions to the reduced value so far and each element in turn.

from operator import mul

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = recude_fn(reduced, x)
    return reduced

def reduce_list(a_func, my_list, initial_value=1):
    for element in my_list:
        initial_value = a_func(initial_value, element)
    return initial_value
        
# The reason we set an initial value is so we can apply each element to a value. (rather than previosu items in the list)

"Sequence Abstractions"



