// 7kyu - Simple consecutive pairs
// 
// Return the count of pairs that have consecutive numbers

// function pairs(ar) {
//     let result = []
//     for (let i = 1; i < ar.length; i += 2) {
//         let b = []
//         if (ar[i] == ar[i - 1] + 1 || ar[i] + 1 == ar[i - 1]) {
//             b.push(ar[i])
//             b.push(ar[i-1])
//             result.push(b)
//         }
//     }
//     return result.length
// }

function pairs(ar) {
    for (var count = 0, i = 1; i < ar.length; i += 2)
        if (ar[i] == ar[i-1] + 1 || ar[i] + 1 == ar[i-1])
            count++
    return count
}

q = pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]) // 3
q
q = pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]) // 2
q
q = pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]) // 0
q
q = pairs([-55, -56, -7, -6, 56, 55, 63, 62]) // 4
q
q = pairs([73, 72, 8, 9, 73, 72]) // 3
q