// 7kyu - Find all non-consecutive numbers

// function allNonConsecutive(arr) {
//     let result = []
//     for (let i = 0; i <= arr.slice(-1); i++) {
//         if ((arr[i] + 1) == arr[i + 1])
//             continue
//         if (arr[i + 1] !== undefined) {
//             result.push({
//                 'i': i + 1,
//                 'n': arr[i + 1]
//             })
//         }
//     }
//     return result
// }

function allNonConsecutive(arr) {
    let result = []
    for (let i = 1; i < arr.length; i++)
        if (arr[i] != arr[i - 1] + 1)
            result.push({i: i, n: arr[i]})
    return result
}

q = allNonConsecutive([1, 2, 3, 4, 6, 7, 8, 10])
q
// Expected: '[{ i: 1, n: -3 }, { i: 3, n: 0 }, { i: 8, n: 6 }, { i: 11, n: 10 }]', 
// tead got: '[{ i: 1, n: -3 }, { i: 3, n: 0 }, { i: 8, n: 6 }]'

// const results = allNonConsecutive([1,2,3,4,6,7,8,10])
// Test.assertSimilar(results, [{i: 4, n:6}, {i: 7, n:10}])