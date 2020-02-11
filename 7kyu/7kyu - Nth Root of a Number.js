// 7kyu - Nth Root of a Number

/* Given two numbers x and n, calculate the (positive) nth root of x.

This means that being r = result, r^n = x  

    Expect inputs greater than 1 × 10^19
    Your function will recieve only positive integers */



const root = (x, n) => Math.pow(x, 1 / n)

q = root(4, 2); // 2 (the square root of 4 is 2 , 2^2 = 4);
q
q = root(8, 3); // 2 (the cube root of 8 is 2   , 2^3 = 8);
q
q = root(256, 4); // 4 (the 4th root of 256 is 4  , 4^4 = 256);
q
q = root(9, 2); // 3 (the square root of 9 is 3 , 3^2 = 9)
q
q = root(6.25, 2) // 2.5
q