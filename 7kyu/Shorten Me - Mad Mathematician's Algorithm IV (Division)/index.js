// 7kyu - Shorten Me: Mad Mathematician's Algorithm IV (Division)

/* Write a madDiv(a,b) function returning a value of a / b without / in your code.
Coding Limitation:
    Less than 30 characters

Input:
    a and b : integer ( 0-10000 )

Note: Only first 10 decimal places will be evaluated. */

madDiv=(a,b)=>a*b**-1

q = madDiv(0, 0) // NaN
q
q = madDiv(1, 2).toFixed(10) // (0.5).toFixed(10)
q
q = madDiv(4, 5).toFixed(10) // (0.8).toFixed(10)
q