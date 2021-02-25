### The reject() function

Implement a function which filters out array values which satisfy the given predicate.
```c
Kata.Reject(new int[] {1, 2, 3, 4, 5, 6}, (n) => n % 2 == 0)  =>  new int[] {1, 3, 5}
