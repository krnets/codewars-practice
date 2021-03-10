### Sqrt approximation

We want to approximate the sqrt function. 

Usually this function takes a floating point number and returns another floating point number, but in this kata we're going to work with integral numbers instead.

Your task is to write a function that takes an integer n and returns either

* an integer k if n is a square number, such that k * k == n or
* a range (k, k+1), such that k * k < n and n < (k+1) * (k+1).

Examples
```
Assert.AreEqual(2, Kata.SqrtApproximation(4));
Assert.AreEqual(new int[] { 2,3 }, Kata.SqrtApproximation(5));
```
Note : pow() and sqrt() functions are disabled.
