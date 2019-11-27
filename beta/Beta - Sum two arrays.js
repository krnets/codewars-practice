// Beta - Sum two arrays 

// Given two arrays of numbers, add the arrays of numbers together

function addArrays(array1, array2) {
    let sum = (array1.join `` * 1) + (array2.join `` * 1)
    let res = [...String(Math.abs(sum))].map(Number)
    res[0] = res[0] * Math.sign(sum)
    return res.length == 1 ? [] : res
}

// const addArrays = (arr1, arr2) => (arr1.length || arr2.length) ? `${(+arr1.join`` + +arr2.join``)}`.match(/-?\d/g).map(Number) : []

q = addArrays([6, 7], [6, 7]) // [ 1, 3, 4 ]
q
q = addArrays([3, 2, 9], [1, 2]) // [3, 4, 1] 
q
q = addArrays([-5, 2, 9], [1, 2])
q