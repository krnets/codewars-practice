// 7kyu - How many consecutive numbers are needed

// function consecutive(arr) {
//     let fullSeq = Math.max(...arr) - Math.min(...arr) + 1
//     let missing = fullSeq - arr.length

//     return Number.isFinite(missing) ? missing : 0
// }

// const consecutive = arr => arr.length && Math.max.apply(0, arr) - Math.min.apply(0, arr) - arr.length + 1

// const consecutive = arr => arr.length ? Math.max(...arr) - Math.min(...arr) - arr.length + 1 : 0

const consecutive = arr => arr.length && Math.max(...arr) - Math.min(...arr) - arr.length + 1

// function consecutive(arr) {
//     arr.sort((a, b) => a - b)
//     for (var missing = 0, i = 0; i <= arr.length; i++) {
//         let diff = arr[i + 1] - arr[i]
//         if (diff > 1)
//             missing += diff - 1
//     }
//     return missing
// }

q = consecutive([4, 8, 6]) // 2
q
q = consecutive([1, 2, 3, 4]) // 0
q
q = consecutive([]) // 0
q
q = consecutive([1]) // 0
q