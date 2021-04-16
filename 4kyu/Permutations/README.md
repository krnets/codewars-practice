### Permutations

In this kata you have to create all permutations of an input string and remove duplicates, if present. 

This means, you have to shuffle all letters from the input in all possible orders.

Examples:
```c
Permutations.SinglePermutations("a"); // => new List {"a"}
Permutations.SinglePermutations("ab"); // => new List {"ab", "ba"}
Permutations.SinglePermutations("aabb"); // => new List {"aabb", "abab", "abba", "baab", "baba", "bbaa"}
```
The order of the permutations doesn't matter.

