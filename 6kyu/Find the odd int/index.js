// 6kyu - Find the odd int

// function findOdd(a) {
//     let count = {}
//     a.forEach(n => count[n] = (count[n] || 0) + 1)
//     let keys = Object.keys(count)
//     let vals = Object.values(count)
//     let res = []

//     for (let i = 0; i < Object.keys(count).length; i++)
//         if (vals[i] % 2 != 0) {
//             res.push(keys[i])
//             break
//         }
//     return +res
// }

// const findOdd = (xs) => xs.reduce((a, b) => a ^ b)

// function findOdd(arr) {
//     return arr.find((item, index) => arr.filter(el => el == item).length % 2)
//   }

//Query the number of times that this 'i' element appears
//then verify if that number of times is odd. If it is true, then return
//that 'i' element

// function findOdd(A) {
//     for (var i = 0; i < A.length; i++) {
//         if ((A.filter(v => v == A[i])).length % 2 != 0)
//             return A[i]
//     }
//     return 0
// }

function findOdd(a) {
    let count = {}
    a.forEach(n => count[n] = (count[n] || 0) + 1)

    for (n in count)
        if (count[n] % 2 != 0)
            return Number(n)
}


q = findOdd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) //  5
q
q = findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) // -1
q
q = findOdd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) //  5
q
q = findOdd([10]) // 10
q
q = findOdd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) // 10
q
q = findOdd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) //  1
q