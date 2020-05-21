// 7kyu - GCD sum

/* Given the sum and gcd of two numbers, return those two numbers in ascending order. 
If the numbers do not exist, return -1, (or return NULL in C).

Given sum = 12 and gcd = 4...
solve(12,4) = [4,8]. The two numbers 4 and 8 sum to 12 and have a gcd of 4.
solve(12,5) = -1. No two numbers exist that sum to 12 and have gcd of 5.
solve(10,2) = [2,8]. Note that [4,6] is also a possibility but we pick the one with the lower first element: 
2 < 4, so we take [2,8]. */

// const gcd = (a, b) => (b == 0 ? a : gcd(b, a % b))

// q = gcd(150, 50)
// q

// const solve = (s, g) => (s % g ? -1 : [g, (s / g - 1) * g])

const solve = (s, g) => s % g ? -1 : [g, s - g]

q = solve(6, 3) // [3,3]
q
q = solve(8, 2) // [2,6]
q
q = solve(10, 3) // -1
q
q = solve(12, 4) // [4,8]
q
q = solve(12, 5) // -1
q
