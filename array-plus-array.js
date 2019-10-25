// function arrayPlusArray(arr1, arr2) {
//     return arr1.reduce((accum, v) => accum + v, 0) +
//            arr2.reduce((accum, v) => accum + v, 0)
// }

function arrayPlusArray(arr1, arr2) {
    return arr1.concat(arr2).reduce((a,b) => a + b, 0)
}

q = arrayPlusArray([1, 2, 3], [4, 5, 6]) // 21);
q
q = arrayPlusArray([-1, -2, -3], [-4, -5, -6]) // -21);
q
q = arrayPlusArray([0, 0, 0], [4, 5, 6]) // 15);
q
q = arrayPlusArray([100, 200, 300], [400, 500, 600]) // 2100);
q