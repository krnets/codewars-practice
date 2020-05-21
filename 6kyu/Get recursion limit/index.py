# 6kyu - Get recursion limit

""" In the sys module there is a function sys.setrecursionlimit and sys.getrecursionlimit. 
These two functions set and get the recursion limit. 
If function calls stack is larger than this limit it will raise a RuntimeError

Examples of these two functions:

import sys
sys.setrecursionlimit(905)
sys.getrecursionlimit() # returns 905
sys.setrecursionlimit(89)
sys.getrecursionlimit() # returns 89

Task
Write a function ```fetch_recursion_limit``` that acts the same as ```sys.getrecursionlimit``` without importing any libraries.

```10 >= Recursion Limit <= 15000```
Hint: Write a separate recursive function  """

def fetch_recursion_limit():
    try:
        return 1 + fetch_recursion_limit()
    except RuntimeError:
        return 2
