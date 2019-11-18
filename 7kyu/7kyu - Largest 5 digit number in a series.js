// 7kyu - Largest 5 digit number in a series

// const solution = digits => String(digits).match(/\d{0,5}/g).reduce((a, b) => a < b ? b : a)

// function solution(digits) {
//     let str = String(digits)
//     let largest = 0
//     for (let i = 0; i < str.length - 4; i++)
//         if (str.substr(i, 5) > largest)
//             largest = str.substr(i, 5)

//     return +largest
// }

function solution(digits) {
    let str = String(digits)
    if (str.length == 5) return digits
    return Math.max(+str.slice(0, 5), solution(str.slice(1)))
}


q = solution(1234567890)
// 67890
q