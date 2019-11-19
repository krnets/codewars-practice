// 7kyu - Count the Combinations 

const numCombo = (arr, num) => arr.filter(v => arr.reduce((x, y) => x + y, -num) == v).length


q = numCombo([2, 0, 0, 0, 1], 2) // 1
q
q = numCombo([2, 0, 0, 0, 1], 1) // 1
q
q = numCombo([2, 0, 0, 0, 1], 3) // 3
q
q = numCombo([0, 0, 0, 0, 0], 0) // 5
q
q = numCombo([0, 0, 0, 0, 1], 1) // 4
q
q = numCombo([0, 0, 0, 0, 1], 2) // 0
q