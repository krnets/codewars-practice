// 6kyu - N smallest elements in original order (performance edition)

/* This challenge is based on the kata by GiacomoSorbi. 
Before doing this one it is advisable to complete the non-performance version first.

You will be given an array of random integers and a number n. You have to extract n smallest integers out of it preserving the original order.

performantSmallest([1, 2, 3, 4, 5], 3)     ===   [1, 2, 3]
performantSmallest([5, 4, 3, 2, 1], 3)     ===   [3, 2, 1]
performantSmallest([1, 2, 3, 4, 1], 3)     ===   [1, 2, 1]
performantSmallest([2, 1, 3, 2, 3], 3)     ===   [2, 1, 2]

    There will be duplicates in the array, and they have to be returned in the order of their each separate appearence.
    This kata is an example of the "know your data" principle. Remember this while searching for the correct approach.

Performance tests

Tests: 20
Array size: 1,300,000
Numbers range: [1; 50]
Number of elements to return: 25-50% of the array */

function performantSmallest(arr, n) {
    let res = []
    let last = {}
    let freq = {}
    arr.forEach(item => freq[item] = ++freq[item] || 1)
    for (let i = 1; i < 50 && n; i++) {
        if (n > freq[i]) {
            n = n - freq[i]
        } else if (freq[i]) {
            last.key = i
            last.count = n
            n = 0
        }
    }
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < last.key) {
            res.push(arr[i])
        } else if (arr[i] == last.key && last.count > 0) {
            res.push(arr[i])
            last.count--
        }
    }
    return res
}

q = performantSmallest([1, 2, 3, 4, 5], 3) // [1,2,3]
q
q = performantSmallest([5, 4, 3, 2, 1], 3) // [3,2,1]
q
q = performantSmallest([1, 2, 3, 4, 1], 3) // [1,2,1]
q
q = performantSmallest([2, 1, 3, 2, 3], 3) // [2,1,2]
q