// 7kyu - Find the stray number

const stray = numbers => numbers.filter(v => numbers.indexOf(v) == numbers.lastIndexOf(v))[0]
// const stray = numbers => numbers.reduce((a, b) => a ^ b)

q = stray([1, 1, 2]) // 2
q
q = stray([17, 17, 3, 17, 17, 17, 17]) // 3
q