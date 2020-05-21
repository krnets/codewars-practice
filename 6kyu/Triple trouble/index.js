// 6kyu - Triple trouble

/* Write a function tripledouble(num1,num2) which takes numbers num1 and num2 and returns 1 if there is a 
straight triple of a number at any place in num1 and also a straight double of the same number in num2.
If this isn't the case, return 0 */

// function tripledouble(num1, num2) {
//     let triple = String(num1).match(/(\d)\1{2}/g)
//     for (let i in triple)
//         if (String(num2).indexOf(triple[i].slice(1)) > -1)
//             return 1
//     return 0
// }

// function tripledouble(num1, num2) {
//     for (let i = 0; i < 10; i++)
//         if (new RegExp(`${i}{3}`).test(num1) && new RegExp(`${i}{2}`).test(num2))
//             return 1
//     return 0
// }

// function tripledouble(num1, num2) {
//     let nums = [...Array(10).keys()]
//     return +nums.some(num =>
//         num1.toString().includes(num.toString().repeat(3)) &&
//         num2.toString().includes(num.toString().repeat(2)))
// }
// const tripledouble = (num1, num2) => +[...Array(10).keys()].some(v => String(num1).includes(String(v).repeat(3)) && String(num2).includes(String(v).repeat(2)))
// const tripledouble = (num1, num2) => +[...Array(10).keys()].some(v => (num1 + '').includes((v + '').repeat(3)) && (num2 + '').includes((v + '').repeat(2)))
// const tripledouble = (num1, num2) => ~~/(.)(\1{2})(?=.*?,.*?\1{2})/.test(num1 + "," + num2)
// const tripledouble = (num1, num2) => +/(.)(\1{2})(?=.*?,.*?\1{2})/.test([num1, num2])
// const tripledouble = (num1, num2) => +/(.)(\1{2})(?=.?,.?\2)/.test([num1, num2])
// const tripledouble = (num1, num2) => +/(\d)\1{2}.*_.*\1{2}/.test(num1 + '_' + num2)
// const tripledouble = (num1, num2) => +/(\d)\1{2}.*,.*\1{2}/.test([num1, num2])
// const tripledouble = (num1, num2) => +/(.)\1{2}.*,.*\1{2}/.test([num1, num2])
// const tripledouble = (num1, num2) => +/(.)\1\1.*,.*\1\1/.test([num1, num2])

function tripledouble(num1, num2) {
    let triple = [...num1+''].filter((v,i,a) => v == a[i+1] && v == a[i-1])
    let double = [...num2+''].filter((v,i,a) => v == a[i+1])
    return +(triple.filter(x => double.find(y => y == x)).length > 0)
}

q = tripledouble(451999278, 41177722899) // 1
q
q = tripledouble(1222345, 12345) // 0
q
q = tripledouble(12345, 12345) // 0
q
q = tripledouble(666789, 12345667) // 1
q
q = tripledouble(10560002, 100) // 1
q
q = tripledouble(1112, 122) // 0
q