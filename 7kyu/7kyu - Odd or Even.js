// 7kyu - Odd or Even?

// const oddOrEven = array => array.reduce((a, b) => a + b, 0) % 2 == 0 ? 'even' : 'odd'
const oddOrEven = array => array.reduce((a, b) => a + b, 0) % 2 ? 'odd' : 'even'
// const oddOrEven = arr => ['even', 'odd'][arr.reduce((a, b) => a + b, 0) & 1]


q = oddOrEven([0]) // 'even'
q
q = oddOrEven([1]) // 'odd'
q
q = oddOrEven([]) // 'even'
q
q = oddOrEven([0, 1, 5]) // 'even'
q
q = oddOrEven([0, 1, 3]) // 'even'
q
q = oddOrEven([1023, 1, 2]) // 'even'
q
q = oddOrEven([0, -1, -5]) // 'even'
q
q = oddOrEven([0, -1, -3]) // 'even'
q
q = oddOrEven([-1023, 1, -2]) // 'even'
q
q = oddOrEven([0, 1, 2]) // 'odd'
q
q = oddOrEven([0, 1, 4]) // 'odd'
q
q = oddOrEven([1023, 1, 3]) // 'odd'
q
q = oddOrEven([0, -1, 2]) // 'odd'
q
q = oddOrEven([0, 1, -4]) // 'odd'
q
q = oddOrEven([-1023, -1, 3]) // 'odd'
q