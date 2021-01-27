### Sum of array singles

In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

Documentation:

Kata.Repeats Method (List<Int32>)

Takes a list where all ints are repeated twice, except two ints, and returns the sum of the ints of a list where those ints only occur once.

Syntax
```c#
public static int Repeats(List<int> source)
```
Parameters

* source
* Type: System.Collections.Generic.List<Int32>
* The list to process.

Return Value

* Type: System.Int32
* The sum of the elements of the list where those elements have no duplicates. 