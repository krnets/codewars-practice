// 5kyu - Bit calculator

// const calculate = (num1, num2) => parseInt(num1, 2) + parseInt(num2, 2)

// const calculate = (num1, num2) => {
//     let sum = 0
//     let num1rev = [...num1].reverse()
//     let num2rev = [...num2].reverse()

//     for (let i = 0, j = 1; i < num1rev.length; i++, j *= 2)
//         if (num1rev[i] == 1)
//             sum += j

//     for (let i = 0, j = 1; i < num2rev.length; i++, j *= 2)
//         if (num2rev[i] == 1)
//             sum += j

//     return sum
// }


const calculate = (num1, num2) => {
    const fromBinary = num => {
        let bit = 1, sum = 0;
        [...num].reverse().forEach((v, i, arr) => {
            if (arr[i] == 1)
                sum += bit
            bit *= 2 })
        return sum
    }
    return fromBinary(num1) + fromBinary(num2)
}


q = calculate("1", "1") // 2
q
q = calculate("10", "10") // 4
q
q = calculate("10", "0") // 2
q
q = calculate("10", "1") // 3
q