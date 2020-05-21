// 7kyu - Shorten Me: Mad Mathematician's Algorithm V (Modulus)

/* Write a madMod(a,b) function returning a value of a % b without % in your code.
Coding Limitation:
    Less than 35 characters
Input: 
    a and b : integer ( 0-10000 ) */

// madMod=(a,b)=>b?Math.abs(a-b):NaN
// madMod=(a,b)=>b?a-b*~~(a/b|0):NaN
// madMod=(a,b)=>b?a-b*(a/b|0):NaN
// madMod=(a,b)=>b?a- ~~(a/b)*b:NaN
// madMod=(a,b)=>a-Math.floor(a/b)*b
madMod=(a,b)=>a-parseInt(a/b)*b

q = madMod(0, 0) // NaN
q
q = madMod(0, 1) // 0
q
q = madMod(1, 2) // 1
q
q = madMod(3, 3) // 0
q
q = madMod(10, 7) // 3
q