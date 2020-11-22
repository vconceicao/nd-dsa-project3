
# Problem 1:  Square Root of an Integer
### Explanation
### Design Decisions:
To find  the floor value of the square root of a number, using binary search concepts. We have to divide the number in two 
and calculate the square of the result and also the square of result + 1, these squares numbers will form a range where we can check if the number we passed as parameter is within this range, we have been found the floor value. If the number is minor than the range of squares, we must assign the result of division -1 to the upper bound or else we must assign the division result + 1 to the lower bound.
### Time Complexity:
The time complexity to find the floor value of a square root takes **O(log n)**, because of each iteration it halves the number possibilities that we are looking.
### Space Complexity:
The Space Complexity of the algorithm is using iterative approach that takes constant time **O(1)**