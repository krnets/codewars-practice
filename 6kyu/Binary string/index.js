// 6ku - Binary string

function toBinaryString(number) {
    let binaryString = ''
    while (number > 0) {
        binaryString = number % 2 + binaryString
        number = Math.floor(number / 2)
    }
    return binaryString || '0'
}

// function toBinaryString(number) {
//     let binaryArray = []
//     while (number > 0) {
//         binaryArray.push(number % 2)
//         number = Math.floor(number / 2)
//     }
//     return binaryArray.reverse().join `` || '0'
// }

// function toBinaryString(number) {
//     let binaryArray = []
//     while (number > 0) {
//         binaryArray.push(number & 1)
//         number >>= 1
//     }
//     return binaryArray.reverse().join `` || '0'
// }

// const toBinaryString = function b(n) {
//     return n > 1 ? b(n >> 1) + n % 2 : n + ''
// }

// const toBinaryString = f = (n, s = '') => n <= 1 ? s || '0' : f(n / 2, ~~(n % 2) + s)

// const toBinaryString = number => number > 1 ? toBinaryString(number >> 1) + number % 2 : String(number)


q = toBinaryString(0) // '0', 'Value passed: 0'
q
q = toBinaryString(6) // '110', 'Value passed: 6'
q
q = toBinaryString(9) // '1001', 'Value passed: 9'
q
q = toBinaryString(15) //  '1111', 'Value passed: 15'
q