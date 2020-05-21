// 8kyu - Multiple of index

// Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

// function multipleOfIndex(array) {
//     return array.reduce((res, v, i) => v % i == 0 ? res.concat(v) : res, [])
// }

function multipleOfIndex(array) {
    return array.filter((v, i) => v % i == 0)
}

q = multipleOfIndex([22, -6, 32, 82, 9, 25]) // [-6, 32, 25]
q
q = multipleOfIndex([68, -1, 1, -7, 10, 10]) // [-1, 10]
q
q = multipleOfIndex([11, -11]) // [-11]
q
q = multipleOfIndex([-56, -85, 72, -26, -14, 76, -27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]) // [-85, 72, 0, 68]
q
q = multipleOfIndex([28, 38, -44, -99, -13, -54, 77, -51]) // [38, -44, -99]
q
q = multipleOfIndex([-1, -49, -1, 67, 8, -60, 39, 35]) // [-49, 8, -60, 35]
q