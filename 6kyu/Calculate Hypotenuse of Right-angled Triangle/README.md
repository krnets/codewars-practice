### Calculate Hypotenuse of Right-angled Triangle

To solve this Kata, complete the function, calculateHypotenuse(a,b), which will return the length of the hyptenuse for a right angled triangle with the other two sides having a length equal to the inputs. More details:

* The returned value should be a number rounded to three decimal places
* An error (ArgumentException in C#) should be thrown if an invalid input is provided (inputs should both be numbers that are above zero)
```c
Kata.CalculateHypotenuse(1,1)           // returns 1.414
Kata.CalculateHypotenuse(3,4)           // returns 5
Kata.CalculateHypotenuse(-2,1)          // throws ArgumentException
Kata.CalculateHypotenuse(2, Double.NaN) // throws ArgumentException
```
For more information on the [hypotenuse](http://en.wikipedia.org/wiki/Hypotenuse)

