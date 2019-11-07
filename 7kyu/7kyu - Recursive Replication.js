// 7kyu - Recursive Replication

// const replicate = (times, number) => (times > 0) ? Array(times).fill(number) : []
const replicate = (times, number) => times > 0 ? [number, ...replicate(times - 1, number)] : []

q = replicate(3, 5) // [5, 5, 5]
q
q = replicate(5, 1) // [1, 1, 1, 1, 1]
q
q = replicate(0, 12) // []
q
q = replicate(-1, 12) // []
q
q = replicate(8, 0) // [0, 0, 0, 0, 0, 0, 0, 0]
q