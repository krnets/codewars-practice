// 6kyu - Sum of many ints

/* Write this function

for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)

You'll need to get a little clever with performance, since n can be a very large number */

// const f = (n, m) => Math.floor(n / m) * ((m * (m - 1)) / 2) + ((n % m) * ((n % m) + 1)) / 2

function gauss(n) {
    return n * (n + 1) / 2
}

function f(n, m) {
    return gauss(m - 1) * (n / m | 0) + gauss(n % m)
}


q = f(10, 5) // 20
q
q = f(20, 20) // 190
q
q = f(15, 10) // 60
q