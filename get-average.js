// const getAverage = arr => Math.floor(arr.reduce((prev, curr) => prev + curr) / arr.length)
// const getAverage = marks => ~~(marks.reduce((s, v) => s + v) / marks.length);
const getAverage = marks => (marks.reduce((s, v) => s + v) / marks.length) | 0

q = getAverage([2,2,2,2]) // 2);
q
q = getAverage([1,2,3,4,5,]) // 3);
q
q = getAverage([1,1,1,1,1,1,1,2]) // 1);
q

