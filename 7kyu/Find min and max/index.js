// 7kyu - Find min and max

function getMinMax(arr) {
    arr.sort((a, b) => a - b)
    return arr.slice(0, 1).concat(arr.slice(-1))
}

// function getMinMax(arr) {
//     arr.sort((a, b) => a - b)
//     return [arr[0], arr[arr.length - 1]]
// }

// const getMinMax = arr => [Math.min(...arr), Math.max(...arr)]

q = getMinMax([1]) // [1,1]
q
q = getMinMax([1, 2]) // [1,2]
q
q = getMinMax([2, 1]) // [1,2]
q