// 7kyu - Get length of the list recursively

// const lenR = x => x.length == 0 ? 0 : 1 + lenR(x.slice(0, x.length - 1))

// const lenR = x => x.length ? 1 + lenR(x.slice(0, x.length - 1)) : 0

// const lenR = x => x.length ? 1 + lenR(x.slice(1)) : 0

// const lenR = x => x.length && 1 + lenR(x.slice(1))
// 
const lenR = ([x, ...xs]) => !x ? 0 : lenR(xs) + 1

// const lenR = (x) => !x[0] ? 0 : lenR(x.slice(1)) + 1

q = lenR([]) // 0
q
q = lenR([1]) // 1
q