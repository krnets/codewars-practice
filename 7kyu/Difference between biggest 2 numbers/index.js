// 7kyu - Difference between biggest 2 numbers

/* You have an array of integers. 
You need to calcurate the difference between 1st biggest number and 2nd biggest number of an array.

    diffBig2([10, 5, 2]);

In this case, 1st biggest number is 10 and 2nd biggest number is 5. So, this function return 5, the result of 10 - 5.
You can assume that the input array must have 2 or more elements.
The input array has the sort() method disabled, so you will have to solve it in another way. */

// function diffBig2(arr) {
//     let res = []
//     for (let i = 0; i < 2; i++) {
//         let max = Math.max(...arr)
//         res.push(max)
//         arr.splice(arr.indexOf(max), 1)
//     }
//     [x, y] = res
//     return x - y
// }

function diffBig2(arr) {
    let max = Math.max(...arr)
    arr.splice(arr.indexOf(max), 1)
    return max - Math.max(...arr)
}

q = diffBig2([2, 1]) // 1
q
q = diffBig2([8, 3, 1]) // 5
q
q = diffBig2([1, 8, 3]) // 5
q