// 7kyu - Factorial division

/* You have to define a function to calculate the division of two factorial numbers. 
This can be useful for large numbers.

In mathematics, the factorial of integer n is written as n!. 
It is equal to the product of n and every integer preceding it. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120.

Some hints: We can see that (n + 1)! = (n + 1) * n!. So (n + 1)! / n! = (n + 1)

We know that 0! = 1 (because n! = (n + 1)! / (n + 1) therefore 0! = 1! / 1 = 1)

And your solution should be able to calculate n! / d!.

*** Please, don't worry about the parameters. 
You will only receive positive integers, and the first one will be greater than the second one */

// const factorialDivision = (n, d) => n == d ? 1 : n * factorialDivision(n - 1, d)

// function factorialDivision(n, d) {
//     for (var x = 1, i = n; i > d; i--)
//         x *= i
//     return x
// }

function factorialDivision(n, d) {
    for (var x = 1; n > d; n--)
        x *= n
    return x
}

q = factorialDivision(5, 3) // 20
q
q = factorialDivision(5, 3) // 20
q
q = factorialDivision(10000, 9999) // 10000
q
q = factorialDivision(98, 90) // 6345015248033280
q