// return an array of numbers (that are a power of 2)
// for which the input "n" is the sum
// const powers = n => {
//     let a = Array(n).fill(0).map((_, i) => i + 1)
//     if (n <= 4) {
//         return [n]
//     }

//     for (let i = 0; i < n; i++) {
//         let c = Math.pow(2,i)
//         let d = Math.pow(2,i+1)

//         if (c + d == n) {
//             return [c, d]
//         } 
//     }
// }
// const powers = n => {
//     let result = n ? [...powers(n & ~-n), n & -n] : []
//     return result.sort((a,b) => a < b)
//     // Number.MAX_SAFE_INTEGER
// }

// const powers = n => {
//     let result = n && powers(n & ~-n) + [, n & -n]
//     return Array.from(result)

// }


// const powers = n => {
//     let s = [];
//     let x = 1;
//     while (n > 0) {
//         if (n % 2 == 1)
//             s.push(x);
//         x *= 2;
//         n = Math.floor(n / 2);
//     }
//     return s;
// }


const powers = n => {
    let result = []
    let v = 1
    while (n > 0) {
        if (n % 2 == 1)
            result.push(v)
        n = Math.floor(n / 2)
        v *= 2
    }
    return result
}

// const powers = n => {
//     return n.toString(2)
//         .split ``
//         .reverse()
//         .map((v, i) => +v ? 2**i : 0)
//         .filter(v => v)
// };




q = powers(100)
q

// q = powers(100)
// q

// q = powers(2) // [2]
// q

// q = powers(1) // [2]
// q
// assert.deepEqual(powers(1), [1])
// assert.deepEqual(powers(2), [2]);
// assert.deepEqual(powers(6), [2, 4]);