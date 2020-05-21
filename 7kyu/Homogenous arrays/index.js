// 7kyu - Homogenous arrays

/* Given a two-dimensional array, return a new array which carries over only those arrays from the original, 
which were not empty and whose items are all of the same type (i.e. homogenous). 
For simplicity, the arrays inside the array will only contain characters and integers.

Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].

Please keep in mind that for this kata, we assume that empty arrays are not homogenous.
The resultant arrays should be in the order they were originally in and should not have its values changed.
No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out. */

function filterHomogenous(arrays) {
    let res = []
    for (let i = 0; i < arrays.length; i++) {
        let type = typeof arrays[i][0]
        if (arrays[i].every(v => typeof v == type))
            res.push(arrays[i])
    }
    return res.filter(v => v.length)
}

// const filterHomogenous = (arrays) => arrays.filter(sub => sub.length > 0 && sub.every(v => typeof v == typeof sub[0]))

q = filterHomogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]) // [[1, 5, 4], ['b']]
q
q = filterHomogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []])  // [[123, 234, 432], ['', 'abc'], [''], ['', '1']]
q