### Retrieve array value by index with default

Complete the solution. It should try to retrieve the value of the array at the index provided. 

If the index is out of the array's max bounds then it should return the default value instead.

Example:
```c
int[] data = new int[] {1, 2, 3};
Kata.Solution(data, 1, -1) => 2
Kata.Solution(data, 5, -1) => -1

// negative values work as long as they aren't out of the length bounds
// if an index is negative, start from the end of the array
Kata.Solution(data, -1, -1) => 3
Kata.Solution(data, -5, -1) => -1
