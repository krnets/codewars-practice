// 7kyu - By 3 or not by 3 - That is the question

// const divisibleByThree = str => [...str].reduce((a, b) => +b + a, 0) % 3 == 0
const divisibleByThree = str => [...str].reduce((a, b) => a + Number(b), 0) % 3 == 0
// const divisibleByThree = str => [...str].reduce((a, b) => a + b * 1, 0) % 3 == 0

q = divisibleByThree('123') // true
q
q = divisibleByThree('19254') // true
q
q = divisibleByThree('88') // false
q
q = divisibleByThree('1') // false
q
q = divisibleByThree('3248238013498536534408923086256176210305002690148677569598600944058832858511179219222468')
q