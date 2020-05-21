// 6kyu - Bit Counting

// const countBits = n => (n.toString(2).match(/1/g) || []).length
const countBits = n => n.toString(2).replace(/0/g, '').length
// const countBits = n => n.toString(2).split('0').join('').length


q = countBits(0) // 0
q
q = countBits(4) // 1
q
q = countBits(7) // 3
q
q = countBits(9) // 2
q
q = countBits(10) // 2
q