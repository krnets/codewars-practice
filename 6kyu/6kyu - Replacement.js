// 6kyu - Replacement

function replacement(a) {
    let max = Math.max(...a)
    a[a.indexOf(max)] = (max > 1) ? 1 : 2
    return a.sort((a, b) => a - b)
}

q = replacement([1, 2, 3, 4, 5]) // [1,1,2,3,4]
q
q = replacement([4, 2, 1, 3, 5]) // [1,1,2,3,4]
q
q = replacement([2, 3, 4, 5, 6]) // [1,2,3,4,5]
q
q = replacement([2, 2, 2]) // [1,2,2]
q
q = replacement([1, 1, 1, 1]) // [1, 1, 2]
q
q = replacement([1, 1]) // [2]
q
q = replacement([1, 1, 1, 2]) // [1, 1, 2]
q
q = replacement([1, 2]) //  [2]
q