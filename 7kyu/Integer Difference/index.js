// 7kyu - Integer Difference

/* Write a function that accepts two arguments: an array of integers and another integer n.
Determine the number of times where two integers in the array have a difference of n.

int_diff([1, 1, 5, 6, 9, 16, 27], 4) # 3 ([1, 5], [1, 5], [5, 9])
int_diff([1, 1, 3, 3], 2) # 4 ([1, 3], [1, 3], [1, 3], [1, 3])

Note: your code should not modify the input array. */

// function intDiff(arr, n) {
//     let count = 0
//     for (let i = 0; i < arr.length - 1; i++)
//         for (let j = i + 1; j < arr.length; j++)
//             if (Math.abs(arr[j] - arr[i]) == n)
//                 count++
//     return count
// }

function intDiff(arr, n) {
    let count = 0
    for (let i = 1; i < arr.length; i++)
        for (let j = 0; j < i; j++)
            if (Math.abs(arr[i] - arr[j]) == n)
                count++
    return count
}

// function intDiff(arr, n) {
//     let count = 0
//     for (let i = 0; i < arr.length; i++)
//         for (let x of arr.slice(i + 1))
//             if (Math.abs(x - arr[i]) == n) count++
//     return count
// }

// const intDiff = ([first, ...rest], n, count = 0) => rest.length ? intDiff(rest, n, count + rest.reduce((a, v) => a + (Math.abs(first - v) == n), 0)) : count
// const intDiff = (arr, n) => arr.length < 2 ? 0 : arr.slice(1).filter(a => Math.abs(a - arr[0]) == n).length + intDiff(arr.slice(1), n)
// const intDiff = (arr, n) => arr.reduce((a, x, i) => a + arr.filter((y, ind) => ind > i && Math.abs(x - y) == n).length, 0)
// const intDiff = (arr, n) => arr.reduce((a, x, i) => a + arr.slice(i + 1).filter(y => Math.abs(x - y) == n).length, 0)

q = intDiff([1, 1, 5, 6, 9, 16, 27], 4) // 3
q
q = intDiff([1, 1, 3, 3], 2) // 4
q