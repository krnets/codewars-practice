// 6kyu - Sum of Digits / Digital Root

/* In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2                          */

const digital_root = n => String(s = [...String(n)].reduce((a, b) => a + Number(b), 0)).length > 1 ? digital_root(s) : s

// function digital_root(n) {
//     return (n - 1) % 9 + 1
// }

// const digital_root = n => --n % 9 + 1

// function digital_root(n) {
//     if (n < 10) return n
//     for (var sum = i = 0, n = String(n); i < n.length; i++)
//         sum += Number(n[i])
//     return digital_root(sum)
// }

// function digital_root(n) {
//     n = eval([...String(n)].join('+'))
//     if (n > 9) return digital_root(n)
//     return n
// }

// function digital_root(n) {
//     if (n < 10) return n
//     return digital_root(n % 10 + digital_root(Math.floor(n / 10)))
// }

// function digital_root(n) {
//     while (n > 9)
//         n = [...String(n)].reduce((a, b) => a + Number(b), 0)
//     return n
// }


q = digital_root(16) // 7
q
q = digital_root(456) // 6
q
q = digital_root(493193) // 2
q
q = digital_root(132189) // 6
q
q = digital_root(942) // 6
q