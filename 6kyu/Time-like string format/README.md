### Time-like string format

Build up a method that takes an integer and formats it to a 'time - like' format.

The method must raise an ArgumentException if its hour length is less than 3 digits and greater than 4.

Example:
```c
Kata.Solution(800); // should return '8:00'
Kata.Solution(1000); // should return '10:00'
Kata.Solution(1451); // should return '14:51'
Kata.Solution(3351); // should return '33:51'
Kata.Solution(10000); // should raise an exception
