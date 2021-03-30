### Largest Cross Sum

Given a matrix, find the cross (row and column) with the largest sum of elements. Return the sum.
```csharp
new int[][]
{
  new int[] {1, 2, 3},
  new int[] {4, 5, 6},
  new int[] {7, 8, 9}
};
// Largest cross is the last column, {3, 6, 9}, with the last row, {7, 8, 9}. 
// Sum of elements is 3 + 6 + 7 + 8 + 9 = 33, therefore Kata.LargestCrossSum(matrix) = 33
``` 
NOTE: the shared element of the column and row should only be counted once.

The matrix may not be square. All elements will be positive integers.

