// 6kyu - Length of missing array

/* You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!

You have to write a method, that return the length of the missing array.
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.
There will always be a missing element and its length will be always between the given arrays.

Algorithms | Basic Language Features | Fundamentals | Arrays */

// function getLengthOfMissingArray(arrayOfArrays) {
//     if (!arrayOfArrays) return 0
//     let a = arrayOfArrays.map(v => v.length)
//     let b = Math.max(...a)
//     let c = Math.min(...a)
//     if (!Number.isFinite(b) || !Number.isFinite(c)) return 0
//     let d = Array(b - c + 1).fill().map((_, i) => i + 1)
//     return d.filter(v => !a.includes(v))[0]
// }

// function getLengthOfMissingArray(arrayOfArrays) {
//     let a = arrayOfArrays ? arrayOfArrays.map(v => v ? v.length : 0) : []
//     if (Math.min(...a) == 0) return 0
//     for (let i = Math.min(...a); i < Math.max(...a); i++)
//         if (!a.includes(i))
//             return i
//     return 0
// }

function getLengthOfMissingArray(arrayOfArrays) {
    let lengths = (arrayOfArrays || []).map(a => a ? a.length : 0).sort((a, b) => a - b)
    if (lengths.includes(0)) return 0
    for (let i = 0; i < lengths.length - 1; i++)
        if (lengths[i] + 1 !== lengths[i + 1])
            return lengths[i] + 1
    return 0
}

// const getLengthOfMissingArray = a => a ? (l = a.map(a => a ? a.length : 0), m = Math.min(...l) | 0, m ? l.reduce((x, n, i) => x ^ n - m ^ i + 1, 0) + m : 0) : 0

q = getLengthOfMissingArray([ [1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9] ]) // 3
q
q = getLengthOfMissingArray([ [5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9] ]) // 2
q
q = getLengthOfMissingArray([ [null], [null, null, null] ]) // 2
q
q = getLengthOfMissingArray([ ['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a', 'a', 'a'] ]) // 5
q
q = getLengthOfMissingArray([]) // 0
q