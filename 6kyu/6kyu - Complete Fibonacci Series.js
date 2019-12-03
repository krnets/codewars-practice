// 6kyu - Complete Fibonacci Series

/* The function 'fibonacci' should return an array of fibonacci numbers. 
The function takes a number as an argument to decide how many no. of elements to produce. 
If the argument is less than or equal to 0 then return empty array

fibonacci(4); // should return [0,1,1,2]
fibonacci(-1); // should return [] */

// function fibonacci(n) {
//     let res = []
//     let [a, b, c] = [0, 0, 1]
//     for (let i = 0; i < n; i++) {
//         [a, b, c] = [b, c, b + c]
//         res.push(a)
//     }
//     return res
// }

// function fibonacci(n) {
//     if (n <= 0) return []
//     if (n == 1) return [0]
//     if (n == 2) return [0, 1]
//     let res = fibonacci(n - 1)
//     res.push(res[res.length - 1] + res[res.length - 2])
//     return res
// }

// function fibonacci(n) {
//     let res = []
//     for (let i = 0; i < n; i++) {
//         if (i > 1) res.push(res[i - 2] + res[i - 1])
//         else if (i === 1) res.push(1)
//         else res.push(0)
//     }
//     return res
// }
function fibonacci(n) {
    if (n <= 0) return []
    let arr = [0, 1]
    for (let i = arr.length; i <= n - 1; i++)
        arr.push(arr[i - 1] + arr[i - 2])
    return arr
}

q = fibonacci(9)
q
q = fibonacci(5).length === 5 // "Expected 5 elements"
q
q = fibonacci(5)[4] === 3 // "Last element for input 5 should be 3"
q
q = fibonacci(13)[12] === 144 //  "Last element for input 13 should be 144"
q
q = fibonacci(-5).length === 0 //  "Expected 0 elements for negative input"
q
q = fibonacci(0).length === 0 //  "Expected 0 elements for 0 input"
q