
# Problem 2: Search in a Rotated Sorted Array
### Explanation
### Design Decisions:
To search in a rotated sorted array, using binary search concepts. I considered the number in the middle as my first location to search. If it  not there, I split the array in two parts. To check in what array I must begin my search, I threated the first and last values of the arrays as a range, where I can check if the number is located. If the number is located in one the arrays, I will use it to find the number using binary search
### Time Complexity:
The time complexity to find a number in a rotated sorted array takes **O(log n)**, because we use binary search that halves the number of the elements to search in the array at each iteration 
### Space Complexity:
The Space Complexity takes constant time  **O(n)** as we are creating some arrays in the solution to help at elements storage. 