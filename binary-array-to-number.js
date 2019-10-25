// const binaryArrayToNumber = arr => parseInt(arr.join ``, 2)
// const binaryArrayToNumber = arr => arr.reduce((a, b) => a << 1 | b)
// const binaryArrayToNumber = arr => arr.reduce((accum, curr) => (accum = accum * 2 + curr), 0)

// const binaryArrayToNumber = arr => arr
//                 // .slice()
//                 .reverse()
//                 .map((x, _) => ({
//                         isBitOn: x === 1,
//                         bitIndex
//                     }))
//                 .filter(x => x.isBitOn)
//                 .map(x => x.bitIndex)
//                 .reduce((acc, val) => acc + Math.pow(2, val), 0)

// const binaryArrayToNumber = arr => {
//     let result = 0
//     for (let i = 0, exponent = arr.length - 1; i < arr.length; i++) {
//         if (arr[i])
//             result += Math.pow(2, exponent)
//         exponent--
//     }
//     return result
// }

// const binaryArrayToNumber = arr => {
//     let result = 0
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[arr.length - i - 1] == 1)
//             result += Math.pow(2, i)
//     }
//     return result
// }

const binaryArrayToNumber = arr => {
    let result = 0
    let binaryPlaceVal = 1
    arr.reverse()
       .map(bit => {
            if (bit === 1)
                result += binaryPlaceVal
            binaryPlaceVal *= 2})
    return result
}

q = binaryArrayToNumber([0, 0, 0, 1]) // 1
q
q = binaryArrayToNumber([0, 0, 1, 0]) // 2
q
q = binaryArrayToNumber([1, 1, 1, 1]) // 15
q
q = binaryArrayToNumber([0, 1, 1, 0]) // 6
q