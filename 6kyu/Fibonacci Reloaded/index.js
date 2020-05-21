// 6kyu - Fibonacci Reloaded

/* And here is Fibonacci again. This time we want to go one step further. 
Our fib() function must be faster! Can you do it? */

function fib(n) {
    [a, b] = [0, 1]
    for (let i = 1; i < n; i++)
        [a, b] = [b, a + b]
    return a
}

q = fib(1) // === 0
q
q = fib(2) // === 1
q
q = fib(3) // === 1
q
q = fib(4) // === 2
q
q = fib(5) // === 3
q