
# Problem 3: Rearrange Array Digits
### Explanation
### Design Decisions:
I've decided to sort the array in the desc order, in that way I can have the major numbers at the first positions. After that I Iterate over the array joining the numbers based in its position in the array to form the two major numbers. 

### Time Complexity:
The sort algorithm used is mergesort  that takes **O(m log n)**, to sort the algorithm and yet I have to iterate over the sorted array to form the two numbers that linear time of **O(n)**. Simplifying at the end we have the time complexity of  **O(m log n)**.

### Space Complexity:
The Space Complexity takes linear time  **O(n)** as we are creating arrays in the solution to help at elements storage. 