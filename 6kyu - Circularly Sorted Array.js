// 6kyu - Circularly Sorted Array

// function isCircleSorted(arr) {
//     for (var res = [], i = 1; i < arr.length + 1; i++)
//         if (arr[i - 1] > arr[i])
//             res.push(arr.splice(i, arr.length))

//     res.push(arr)
//     let a = res.reduce((x, y) => x.concat(y))

//     for (let i = 0; i < a.length; i++)
//         if (a[i] > a[i + 1])
//             return false

//     return true
// }

// function isCircleSorted(arr) {
//     for (let i = 0, flag = false; i < arr.length; i++) {
//         if (arr[i] > arr[(i + 1) % arr.length]) {
//             if (flag)
//                 return false
//             flag = true
//         }
//     }
//     return true
// }

function isCircleSorted(arr) {
    for (var count = 0, i = 0; i < arr.length; i++)
        if (arr[i] > arr[(i + 1) % arr.length])
            count++
    return count < 2
}

// const isCircleSorted = (arr) => arr.map((v, i) => v <= arr[(i + 1) % arr.length]).filter(v => !v).length < 2
// const isCircleSorted = (arr) => arr.filter((v, i) => v > arr[(i + 1) % arr.length]).length < 2
// const isCircleSorted = (arr) => arr.reduce((a, v, i) => a + (v > arr[(i + 1) % arr.length]), 0) < 2


q = isCircleSorted([2, 3, 4, 4, 6, 6, -8, -3, 0, 1])
q
q = isCircleSorted([2, 3, 4, 1]) // true
q
q = isCircleSorted([2, 3, 4, 5, 6]) // true
q
q = isCircleSorted([6, 2, 3, 4, 5]) // true
q
q = isCircleSorted([3, 2, 4, 5, 6]) // false
q