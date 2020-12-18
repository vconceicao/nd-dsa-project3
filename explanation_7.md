# Problem 7: Request Routing in a Web Server with a Trie
### Explanation
### Design Decisions:
This solution uses **trie** to  implement a HTTP Router. It splits the path into parts, so we have less nodes in the **trie** comparing if we store all the characters of the path. 

### Time Complexity:
As I said the this solution is using **trie** and it has time complexity of **O(n)** 

### Space Complexity:
The Space Complexity takes linear time  **O(n)** at worst cases, considering the numbers of distinct paths inside the dictionary.