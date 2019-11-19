// Beta - Number of ones in binary

// Write a function which takes a positive integer and returns the number of ones that appear in its binary representation. 

const ones = n => (+n).toString(2).split(0).join``.length
// const ones = n => n.toString(2).match(/1/g).length

q = ones(1) // 1
q
q = ones(4) // 1
q
q = ones(7) // 3
q