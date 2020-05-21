// 7kyu - Get list sum recursively

// const sumR = x => !x[0] ? 0 : x[0] + sumR(x.slice(1))

// const sumR = x => x[0] ? x[0] + sumR(x.slice(1)) : 0

const sumR = x => x[0] ? x.shift() + sumR(x) : 0

q = sumR([]) // 0
q
q = sumR([1]) // 1
q
q = sumR([1, 1, 1]) // 3
q
q = sumR([5, 1, 2]) // 8
q