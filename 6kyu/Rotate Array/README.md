### Rotate Array (JS)

Note: This kata is a translation of this (Java) one: http://www.codewars.com/kata/rotate-array. 

Create a function named "rotate" that takes an array and returns a new one with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. 

If n is less than 0 it should rotate the array to the left. 

If n is 0, then it should return the array unchanged.

Example:
```csharp
var data = new object[] { 1, 2, 3, 4, 5 };

Kata.Rotate(data, 1); // => [5, 1, 2, 3, 4]
Kata.Rotate(data, 2); // => [4, 5, 1, 2, 3]
Kata.Rotate(data, 3); // => [3, 4, 5, 1, 2]
Kata.Rotate(data, 4); // => [2, 3, 4, 5, 1]
Kata.Rotate(data, 5); // => [1, 2, 3, 4, 5]

Kata.Rotate(data, 0); // => [1, 2, 3, 4, 5]

Kata.Rotate(data, -1); // => [2, 3, 4, 5, 1]
Kata.Rotate(data, -2); // => [3, 4, 5, 1, 2]
Kata.Rotate(data, -3); // => [4, 5, 1, 2, 3]
Kata.Rotate(data, -4); // => [5, 1, 2, 3, 4]
Kata.Rotate(data, -5); // => [1, 2, 3, 4, 5]
```
Furthermore the method should take ANY array of objects and perform this operation on them:
```csharp
Kata.Rotate(new object[] { 'a', 'b', 'c' }, 1);     // => ['c', 'a', 'b']
Kata.Rotate(new object[] { 1.0, 2.0, 3.0 }, 1);     // => [3.0, 1.0, 2.0]
Kata.Rotate(new object[] { true, true, false }, 1); // => [false, true, true]
```
Finally the rotation shouldn't be limited by the indices available in the array. Meaning that if we exceed the indices of the array it keeps rotating.

Example:
```csharp
var data = new object[] { 1, 2, 3, 4, 5 };

Kata.Rotate(data, 7);     // => [4, 5, 1, 2, 3]
Kata.Rotate(data, 11);    // => [5, 1, 2, 3, 4]
Kata.Rotate(data, 12478); // => [3, 4, 5, 1, 2]
