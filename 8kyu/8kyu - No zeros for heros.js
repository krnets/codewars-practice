// 8kyu - No zeros for heros

/* Numbers ending with zeros are boring.
They might be fun in your world, but not here.
Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105

Zero alone is fine, don't worry about it. Poor guy anyway */


// function noBoringZeros(n) {
//     let a = String(n).split('').reverse()
//     for (let i = 0; i < a.length; i++) {
//         while (a[i] == 0)
//             a.splice(0, 1)
//         if (a[i] != 0)
//             break
//     }
//     return Number(a.reverse().join(''))
// }

// function noBoringZeros(n) {
//     while (n % 10 == 0 && n != 0)
//         n /= 10
//     return n
// }

const noBoringZeros = (n) => +`${n}`.replace(/0*$/, '')

q = noBoringZeros(1450) // 145
q
q = noBoringZeros(960000) // 96
q
q = noBoringZeros(1050) // 105
q
q = noBoringZeros(-1050) // -105
q
q = noBoringZeros(-105) // -105
q
q = noBoringZeros(0) // 0
q