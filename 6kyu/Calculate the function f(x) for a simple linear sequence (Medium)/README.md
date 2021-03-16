### Calculate the function f(x) for a simple linear sequence (Medium)

For any given linear sequence, calculate the function [f(x)] and return it as a function.

For example:
```
GetFunction(new[] { 0, 1, 2, 3, 4 })(5) => 5
GetFunction(new[] { 0, 3, 6, 9, 12 })(10) => 30
GetFunction(new[] { 1, 4, 7, 10, 13 })(20) => 61
```
Assumptions for this kata are:

* The sequence argument will always contain 5 values equal to f(0) - f(4).
* The function will always be in the format "nx +/- m", 'x +/- m', 'nx', 'x' or 'm'
* If sequence is non-linear, throw an ArgumentException.
