// function check(a,x) {
//     return a.some(val => val == x)
// }

// const check = (a,x) => a.indexOf(x) >= 0;
const check = (a,x) => a.indexOf(x) != -1

// const check = (a,x) => a.includes(x)

// const check = Function.prototype.call.bind(Array.prototype.includes)

q = check([66, 101], 66) //, true
q
q = check([80, 117, 115, 104, 45, 85, 112, 115], 45) //, true
q
q = check(['t', 'e', 's', 't'], 'e') //, true
q
q = check(['what', 'a', 'great', 'kata'], 'kat') // false
q