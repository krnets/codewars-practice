// 6kyu - N-th Fibonacci

/* Write a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

   nthFibo(4) == 2

Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. */

function nthFibo(n) {
    [a, b] = [0, 1]
    for (let i = 1; i < n; i++)
        [a, b] = [b, a + b]
    return a
}

// const nthFibo = n => n < 2 ? 0 : n == 2 ? 1 : nthFibo(n - 1) + nthFibo(n - 2)

// const SQRT5 = Math.sqrt(5);
// const PHI = (SQRT5 + 1) / 2;
// const ithFibo = i => Math.round(PHI**i / SQRT5);
// const nthFibo = n => ithFibo(n - 1);

q = nthFibo(4) // 2
q
q = nthFibo(5) // 3
q
q = nthFibo(6) // 5
q
q = nthFibo(9) // 21
q
q = nthFibo(15) // 377
q