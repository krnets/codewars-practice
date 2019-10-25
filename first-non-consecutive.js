// const firstDup = s => s.split('').filter((x, _, a) => a.indexOf(x) !== a.lastIndexOf(x))[0] || null;
// const firstNonRepeated = s => [...s].filter(e => s.indexOf(e) === s.lastIndexOf(e))[0] || null;

// function firstNonConsecutive(arr) {
//     let a = arr.map((v, i) => arr[i] - i)
//     a
//     let j = a[0]
//     j
//     for (let i = 0; i < a.length; i++) {
//         if (a[0] != a[i]) {
//             return arr[i]
//         }
//     }
//     return null
// }

function firstNonConsecutive(arr) {
    for (let i = 0; i < arr.length; i++)
        if (arr[i] - arr[0] != i)
            return arr[i]
    return null
}



q = firstNonConsecutive([1, 2, 3, 4, 6, 7, 8]) // 6
q
q = firstNonConsecutive([1, 2, 3, 4, 5, 6, 7]) // undefined
q
q = firstNonConsecutive([]) // 0
q
q = firstNonConsecutive([3, 4, 5, 6, 7, 9]) // undefined
q