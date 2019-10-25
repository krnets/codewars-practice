const sumAverage = arr => Math.floor(arr.map(subArr => subArr.reduce((a, b) => a + b, 0) / subArr.length).reduce((a, b) => a + b, 0))


// q = sumAverage([3, 4, 1, 3, 5, 1, 4])
// q
q = sumAverage([
    [3, 4, 1, 3, 5, 1, 4],
    [21, 54, 33, 21, 77]
]) // 44
q
q = sumAverage([
    [-4, 3, -8, -2],
    [2, 9, 1, -5],
    [-7, -2, -6, -4]
]) // -6
q