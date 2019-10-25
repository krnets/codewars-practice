// const positiveSum = (arr) => arr.filter(v => v > 0).reduce((accum, v) => accum + v, 0)
const positiveSum = (arr) => arr.reduce((accum, v) => v > 0 ? v + accum : accum, 0)

q = positiveSum([1, 2, 3, 4, 5]) // 15
q
q = positiveSum([1, -2, 3, 4, 5]) // 13
q
q = positiveSum([]) // 0
q
q = positiveSum([-1, -2, -3, -4, -5]) // 0
q
q = positiveSum([-1, 2, 3, 4, -5]) // 9
q