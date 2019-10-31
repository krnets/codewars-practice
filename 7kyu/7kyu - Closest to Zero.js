// 7kyu - Closest to Zero

// const closest = arr => {
//     let posNums = arr.filter(v => v > 0).sort((a, b) => a - b) 
//     let negNums = arr.filter(v => v < 0).sort((a, b) => b - a)

//     return arr.includes(0) ? 0 :
//         Math.abs(negNums[0]) == posNums[0] ? null :
//         posNums.length == 0 || Math.abs(negNums[0]) <  posNums[0] ? negNums[0] : 
//         posNums[0]
// }


function closest(arr) {
    arr = arr.sort((a, b) => Math.abs(a) - Math.abs(b))
    for (let i = 1; i < arr.length; i++)
        if (arr[0] + arr[i] == 0) return null
    return arr[0]
}


// const closest = arr => arr.sort((a, b) => Math.abs(a) - Math.abs(b))
//                           .includes(0) ? 0 :
//                           arr[0] + arr[1] == 0 ? null :
//                           arr[0]



q = closest([-42, -105, -42])
q
q = closest([10, 3, 9, 1]) // 1
q
q = closest([2, 4, -1, -3]) // -1
q
q = closest([13, 0, -6]) // 0
q
q = closest([5, 1, -1, 2, -10]) // null
q
q = closest([5, 11, 11, 2, -1, 1]) // null
q