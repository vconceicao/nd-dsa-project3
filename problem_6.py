import sys
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return ()
        
    min = sys.maxsize
    max = -sys.maxsize - 1
    index = 0

    while index < len(ints):
        if ints[index] > max:
            max = ints[index]

        if ints[index] < min:
            min = ints[index]

        index+=1
    
    return min, max

## Example Test Case of Integers

l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l1)
print ("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")
#(0, 9)

l2 = [i for i in range(10, 100)]  # a list containing 10 - 99
random.shuffle(l2)
print ("Pass" if ((10, 99) == get_min_max(l2)) else "Fail")
#(10, 99)
l3 = [i for i in range(-10, 1)]  # a list containing -10 - 0
random.shuffle(l3)
print ("Pass" if ((-10, 0) == get_min_max(l3)) else "Fail")
#(-10, 1)
l4 = []  # a list containing nothing
random.shuffle(l4)
print ("Pass" if (() == get_min_max(l4)) else "Fail")
#()