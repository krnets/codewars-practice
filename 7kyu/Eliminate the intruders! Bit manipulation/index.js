// 7kyu - Eliminate the intruders! Bit manipulation

const eliminateUnsetBits = number => parseInt(number.replace(/0/g, ''), 2) || 0
// const eliminateUnsetBits = number => parseInt(number.replace(/0/g, '') || 0, 2)

q = eliminateUnsetBits("11010101010101") // 255
q
q = eliminateUnsetBits("111") // 7
q
q = eliminateUnsetBits("1000000") // 1
q
q = eliminateUnsetBits("000") // 0
q