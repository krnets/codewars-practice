### Area of a Circle

Complete the function circleArea so that it will return the area of a circle with the given radius. Round the returned number to two decimal places (except for Haskell). If the radius is not positive or not a number, return false.

Example:
```c
Kata.CalculateAreaOfCircle("-123"); //throws ArgumentException
Kata.CalculateAreaOfCircle("0"); //throws ArgumentException
Kata.CalculateAreaOfCircle("43.2673"); //return 5881.25
Kata.CalculateAreaOfCircle("68"); //return 14526.72
Kata.CalculateAreaOfCircle("number"); //throws ArgumentException
