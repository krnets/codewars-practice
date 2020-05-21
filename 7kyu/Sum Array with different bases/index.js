// 7kyu - Sum Array with different bases

// const sumItUp = numbersWithBases => numbersWithBases.map(v => parseInt(v[0], v[1])).reduce((a, b) => a + b, 0)
// const sumItUp = numbersWithBases => numbersWithBases.reduce((a, b) => a + parseInt(b[0], b[1]), 0)
const sumItUp = numbersWithBases => numbersWithBases.reduce((a, [n, b]) => a + parseInt(n, b), 0)

q = sumItUp([["101",2], ["10",8]]) // 13
q
q = sumItUp([["ABC",16], ["11",2]]) // 2751
q
q = sumItUp([["101",16],["7640",8],["1",9]]) // 4258
q