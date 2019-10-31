const sumCubes = n => Array(n).fill(0).map((v, i) => Math.pow(i + 1, 3)).reduce((a, b) => a + b)
// const sumCubes = n => [...Array(n + 1).keys()].reduce((r, i) => r + i ** 3);


q = sumCubes(1)
q
q = sumCubes(2)
q
q = sumCubes(3)
q
q = sumCubes(4)
q
q = sumCubes(5)
q
q = sumCubes(6)
q
q = sumCubes(7)
q

// [ [1, 1], [2, 9], [3, 36], [4, 100], [10, 3025], [123, 58155876] ].forEach(([n,exp]) => Test.assertEquals(sumCubes(n), exp))