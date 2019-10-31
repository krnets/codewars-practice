const closestMultiple10 = num => Math.round(num / 10) * 10

// const closestMultiple10 = num => {
//     return num % 10 >= 5 ? Math.ceil(num / 10) * 10 : Math.floor(num / 10) * 10;
// }

q = closestMultiple10(2010) // 50
q
q = closestMultiple10(20100) // 50
q
q = closestMultiple10(50) // 50
q
q = closestMultiple10(51) // 50
q
q = closestMultiple10(52) // 50
q
q = closestMultiple10(53) // 50
q
q = closestMultiple10(54) // 50
q
q = closestMultiple10(55) // 60
q
q = closestMultiple10(56) // 60
q
q = closestMultiple10(57) // 60
q
q = closestMultiple10(58) // 60
q
q = closestMultiple10(59) // 60
q