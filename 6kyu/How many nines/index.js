// 6kyu - How many nines?

/* Ask a mathematician: "What proportion of natural numbers contain at least one digit 9 somewhere in their decimal representation?"
Clearly though, not all whole numbers contain a 9.
In this kata we ask the question: "How many Integers in the range [0..n] contain at least one 9 in their decimal representation?"
In other words, write the function:

nines :: BigInt => BigInt

Where, for example:

nines(1n)  = 0n
nines(10n) = 1n     // 9
nines(90n) = 10n    // 9, 19, 29, 39, 49, 59, 69, 79, 89, 90

When designing your solution keep in mind that your function will be tested against some large numbers (up to 10^38)
Puzzles | Numbers | Mathematics | Algorithms */

function nines(n) {
    if (n < 10n) return n == 9 ? 1n : 0n
    let str = String(n)
    let len = BigInt(str.length - 1)
    let head = BigInt(str[0])
    let tail = BigInt(str.slice(1))
    let recur = head == 9 ? tail + 1n : nines(tail)
    let f = n => n == 1 ? 1n : 10n ** (--n) + 9n * f(n)
    return head * f(len) + recur
}

q = nines(1n) // 0n
q
q = nines(10n) // 1n
q
q = nines(100n) // 19n
q
q = nines(1000n) // 271n
q
q = nines(3950n) // 1035n
q