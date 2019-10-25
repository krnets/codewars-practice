// function numberToMoney(n) {
//     let aa = Math.floor(n * 100) / 100
//     aa
//     let a = aa.toLocaleString()
//     a
//     return a
// }

const numberToMoney = n => (Math.trunc(n * 100) / 100).toLocaleString()

q = numberToMoney(2546.2562) //     '2,546.25'
q
q = numberToMoney(1500.342626) // '1,500.34'
q
q = numberToMoney(100.2134) //     '100.21'
q