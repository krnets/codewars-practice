// 7kyu - Operations with sequence

/* Steps

    Square the numbers that are greater than zero.
    Multiply by 3 every third number.
    Multiply by -1 every fifth number.
    Return the sum of the sequence.

Example
{ -2, -1, 0, 1, 2 } returns -6

1. { -2, -1, 0, 1 * 1, 2 * 2 }
2. { -2, -1, 0 * 3, 1, 4 }
3. { -2, -1, 0, 1, -1 * 4 }
4. -6

P.S.: The sequence consists only of integers. And try not to use "for", "while" or "loop" statements. */

const calc = arr => arr
    .map(v => v > 0 ? v * v : v)
    .map((v, i) => (i + 1) % 3 == 0 ? v * 3 : v)
    .map((v, i) => (i + 1) % 5 == 0 ? v * -1 : v)
    .reduce((a, b) => a + b, 0)

q = calc([0, 2, 1, -6, -3, 3]) // 31
q
q = calc([0]) // 0
q
q = calc([1, 1, 1, 1, 1]) // 5
q