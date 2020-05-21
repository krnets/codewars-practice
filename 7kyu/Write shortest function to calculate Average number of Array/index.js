// 7kyu - Write shortest function to calculate Average number of Array

// const avg = a => a.reduce((t, c) => t + c, 0) / a.length
const avg = a => eval(a.join('+')) / a.length

q = avg([0, 1, 2, 3, 4]) // 2, "returns valid avg number"
q