# Problem 5: Autocomplete with Tries
### Explanation
### Design Decisions:
A Trie is data-structure good for re**trie**val of data.  It offers advantage over other data-structures in space complexity as it works overlappings characters when storing (words)strings. It's often used in spell-checker and auto-complete features.


### Time Complexity:
To insert in the Trie, we have to consider the **lenght of the input** **O(n)** as we have to iterate through it to add the chars invidually in each node. Each node itself has a **dictionary** to store other nodes, because of it we have to check if the char is in the dictionary, **O(d)** is the size of the dictionary. At the end, we have **O(n*d)**.  

Find function has the same time complexity of insert function taking in consideration the lenght of the input and length of the dictionary. **O(n*d)**

Suffixes function is using recursive calls in each node to collect the chars and converting them into words. We have to consider the iteration of each key of the dictionary **O(n)** and the recursive calls using the keys **O(m)**. A the end we have **O(n*m)**

### Space Complexity:
The Space Complexity takes linear time  **O(n)** at worst cases, considering the numbers of chars of the alphabet that can be in the dictionary.