// 7kyu - Recursion #2 - Fibonacci

/* In mathematical terms, the sequence f(n) of fibonacci numbers is defined by the recurrence relation

f(n) = f(n-1) + f(n-2)

with seed values

f(1) = 1 and f(2) = 1

You have to create the function fibonacci that receives n and returns f(n). You have to use recursion. */

// let cache = { 1: 1, 2: 1 }

// const fibonacci = (n) => cache[n] || (cache[n] = fibonacci(n - 1) + fibonacci(n - 2))

// const fibonacci = (n) => (n == 0) ? 0 : (n == 1) ? 1 : fibonacci(n-1) + fibonacci(n-2)


// const fibCache = [0, 1, 1]

// const fibonacci = n => fibCache[n] || (fibCache[n] = fibonacci(n - 1) + fibonacci(n - 2))

// q = fibCache.length
// q
// q = fibonacci(8)
// q
// q = fibCache.length
// q
// fibCache
// q = fibonacci(21)
// q
// q = fibCache.length
// q

const fibonacci = (n) => n > 1 ? fibonacci[n] || (fibonacci[n] = fibonacci(n - 1) + fibonacci(n - 2)) : n


q = fibonacci(1) // 1
q
q = fibonacci(2) // 1
q
q = fibonacci(3) // 2
q
q = fibonacci(4) // 3
q
q = fibonacci(8) // 21
q
q = fibonacci(21) // 10946
q
q = fibonacci(25) // 75025
q
q = fibonacci(42) // 267914296
q
q = fibonacci(82) // 61305790721611580
q