### Normalizing Out of Range Array Indexes

Implement a function that normalizes out of range sequence indexes (converts them to 'in range' indexes) by making them repeatedly 'loop' around the array. The function should then return the value at that index. Indexes that are not out of range should be handled normally and indexes to empty sequences should return undefined/None depending on the language.

For positive numbers that are out of range, they loop around starting at the beginning, so
```c
Kata.NormIndex(arr, arr.Length);     //Returns first element
Kata.NormIndex(arr, arr.Length + 1); //Returns second element
Kata.NormIndex(arr, arr.Length + 2); //Returns third element
//And so on...
Kata.NormIndex(arr, arr.Length * 2); //Returns first element
```c
For negative numbers, they loop starting from the end, so
```c
Kata.NormIndex(arr, -1);    //Returns last element
Kata.NormIndex(arr, -2);    //Returns second to last element
Kata.NormIndex(arr, -3);    //Returns third to last element
//And so on...
Kata.NormIndex(arr, -arr.Length); //Returns first element
