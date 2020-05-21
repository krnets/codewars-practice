// 7kyu - One Line: Even Check

/* Create a function that accepts a number n as a parameter and 
returns true if the number is even and false if the number is odd.
 1 <= n <= 1000 ``` 
The length of your code must be less than or equal to 19 characters.
You are not allowed to use %. */


evenCheck=n=>!(n&1)


q = evenCheck(6) // true
q
q = evenCheck(8) // true
q
q = evenCheck(7) // false
q
q = evenCheck(100) // true
q