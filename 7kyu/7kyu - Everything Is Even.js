// 7kyu - Everything Is Even

/* Write a function that will convert any number to its nearest even number. 
When the number is halfway between two even numbers it should round away from zero. */

function ensureEven(n) {
    for (let i = n;; n <= 0 ? i-- : i++)
        if (Math.round(i) % 2 == 0)
            return Math.round(i)
}

// const ensureEven = n => n % 2 ? n << 1 : n
// const ensureEven = n => ~~(~~n + n % 2)
// const ensureEven = n => Math.round(n) % 2 + Math.round(n)

q = ensureEven(1) // 2
q
q = ensureEven(0.5) // 0
q
q = ensureEven(-1) // -2
q
q = ensureEven(-0.5) // 0
q