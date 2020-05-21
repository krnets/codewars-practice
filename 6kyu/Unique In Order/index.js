// 6kyu - Unique In Order


// function uniqueInOrder(iterable) {
//     let result = []
//     let previous
//     for (let i = 0; i < iterable.length; i++)
//         if (iterable[i] != prev) {
//             prev = iterable[i]
//             res.push(prev)
//         }
//     return res
// }

function uniqueInOrder(iterable) {
    let previous
    let result = []
    for (let v of iterable) 
        if (v != previous) {
            previous = v
            result.push(v)
        }
    return result
}

// function uniqueInOrder(iterable) {
//     if (typeof iterable == 'string') iterable = [...iterable]
//     return iterable.filter((_, i, arr) => arr[i] != arr[i+1])
// }

// const uniqueInOrder = iterable => [...iterable].filter((v, i) => v != iterable[i-1])


q = uniqueInOrder('AAAABBBCCDAABBB')
// ['A','B','C','D','A','B'])
q
q = uniqueInOrder('ABBCcAD')
// ['A', 'B', 'C', 'c', 'A', 'D']
q
q = uniqueInOrder([1, 2, 2, 3, 3])
// [1,2,3]
q