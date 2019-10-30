// 7kyu - Minimum Steps - Array Series 6

// const minimumSteps = (numbers, value) => {
//     let countSteps = -1
//     let accum = 0
//     numbers.sort((a, b) => a - b).forEach(v => {
//         if (accum >= value)
//             return countSteps
//         else {
//             accum += v
//             countSteps++
//         }
//     })
//     return countSteps
// }

// function minimumSteps(numbers, value) {
//     numbers.sort((a, b) => a - b)
//     for (let i = 0, sum = 0; i < numbers.length; i++) {
//         sum += numbers[i]
//         if (sum >= value)
//             return i
//     }
// }

const minimumSteps = (numbers, value) => numbers.sort((a, b) => a - b).filter(n => (value -= n) > 0).length

q = minimumSteps([4, 6, 3], 7) // 1 
q
q = minimumSteps([10, 9, 9, 8], 17) // 1
q
q = minimumSteps([8, 9, 10, 4, 2], 23) // 3
q
q = minimumSteps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464) // 8
q
q = minimumSteps([4, 6, 3], 2) // 0
q