// 7kyu - ATM

/* There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
You are given money in nominal value of n with 1<=n<=1500.
Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible. */

function solve(n) {
    let count = 0
    while (n >= 500) { count++; n -= 500 }
    while (n >= 200) { count++; n -= 200 }
    while (n >= 100) { count++; n -= 100 }
    while (n >= 50)  { count++; n -= 50  }
    while (n >= 20)  { count++; n -= 20  }
    while (n >= 10)  { count++; n -= 10  }
    return n == 0 ? count : -1
}

// const solve = n => n % 10 ? -1 : n ? solve(n - [500, 200, 100, 50, 20, 10].find(v => v <= n)) + 1 : 0

// function solve(n) {
//     if (n % 10) return -1
//     return [500, 200, 100, 50, 20, 10].reduce((count, v) => {
//         let res = Math.floor(n / v);
//         n = n % v;
//         return count + res
//     }, 0)
// }

// function solve(n) {
//     let count = 0
//     for (denomination of [500,200,100,50,20,10]) {
//         count += Math.floor(n / denomination)
//         n %= denomination
//     }
//     return n == 0 ? count : -1
// }

q = solve(500) // 1
q
q = solve(770) // 4
q
q = solve(550) // 2
q
q = solve(10) // 1
q
q = solve(1250) // 4
q
q = solve(5000) // 10
q
q = solve(125) // -1
q
q = solve(666) // -1
q
q = solve(42) // -1
q