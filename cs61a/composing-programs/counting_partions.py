# Cpunting partitions of an integer is one problem that is very difficult to solve without using recursion
# The number of partitions of a positive integer n, using parts up to size m, if the number of ways of ways n can be expressed as the sum of positive integer parts up to m in increasing order.
""" 
>> count_paritions(n=6, using_parts_up_to_size_n=4)

2 + 4 = 6
1 + 1 + 4 = 6
3 + 3 = 6
1 + 2 + 3 = 6
1 + 1 + 1 + 3 = 6
2 + 2 + 2 = 6
1 + 1 + 2 + 2 = 6 
1 + 1 + 1 + 1 + 2 = 6
1 + 1 + 1 + 1 + 1 + 1 = 6

should return 9
"""
# Notice how all parts are less than 4 and the go in increasing order from lowest values/ lowest parts to highest values /highest parts

# This is the number of different ways we can break 6 into groups with values less than 4

""" How to solve the problem """
# - Use recusive decompisition to find simpiler instances of the problem
# - Explore to different possibilities:
#     - use at least 1 group of 4
#     - dont use any 4's
# - Solve two simpler problems
# - count_paritions(2, 4)
# - count_paritions(6, 3)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0 
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, n)
        without_m = count_partitions(n, m-1)
        return with_m + without_m


    
