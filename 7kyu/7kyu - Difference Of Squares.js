// 7kyu - Difference Of Squares

/* Find the difference between the sum of the squares of the 
first n natural numbers (1 <= n <= 100) and the square of their sum.

For example, when n = 10:
    The square of the sum of the numbers is:
    (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) ** 2 = 55 ** 2 = 3025

    The sum of the squares of the numbers is:
    12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385

Hence the difference between square of the sum of the first ten natural numbers 
and the sum of the squares of those numbes is: 3025 - 385 = 2640 */

function differenceOfSquares(n) {
    let arr = Array(n).fill().map((_, i) => i + 1)
    let squareOfSums = arr.reduce((a, b) => a + b, 0) ** 2
    let sumOfSquares = arr.reduce((a, b) => a + b ** 2, 0)
    return squareOfSums - sumOfSquares
}

q = differenceOfSquares(5) // 170
q
q = differenceOfSquares(10) // 2640
q
q = differenceOfSquares(100) // 25164150
q