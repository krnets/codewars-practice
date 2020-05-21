// 7kyu - Sum and Multiply

/* Write a function that accepts two parameters (sum and multiply) and find two numbers [x, y], where x + y = sum and x * y = multiply.

sum = 12 and multiply = 32
In this case, x equals 4 and y equals 8.
x = 4
y = 8
Because
x + y = 4 + 8 = 12 = sum
x * y = 4 * 8 = 32 = multiply
The result should be [4, 8].
0 <= x <= 1000
0 <= y <= 1000

If there is no solution, your function should return null.
You should return an array containing the two values [x, y] and it should be sorted in ascending order.
One last thing: x and y are integers (no decimals). Algorithms | Numbers */

function sumAndMultiply(sum, multiply) {
    for (let i = 0; i <= sum; i++)
        for (let j = 0; j <= i; j++)
            if (i + j == sum && i * j == multiply)
                return [j, i]
    return null
}

q = sumAndMultiply(13, 12), [1, 12]
q
q = sumAndMultiply(6, 9), [3, 3]
q
q = sumAndMultiply(200, 8452), null
q
q = sumAndMultiply(15, 56), [7, 8]
q