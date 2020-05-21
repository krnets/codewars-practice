// 7kyu - Averages of numbers

// function averages(numbers) {
//     if (!numbers) return []
//     for (var res = [], i = 0; i < numbers.length - 1; i++)
//         res.push((numbers[i] + numbers[i + 1]) / 2)
//     return res
// }

// function averages(numbers) {
//     if (numbers) 
//         for (var res = [], i = 0; i < numbers.length - 1; i++)
//             res.push((numbers[i] + numbers[i+ 1]) / 2)
//     return res
// }

const averages = numbers => numbers ? numbers.slice(1).map((v, i) => (v + numbers[i]) / 2) : []
// const averages = numbers => numbers ? numbers.map((v, i, a) => (v + a[i + 1]) / 2).slice(0, -1) : []
// const averages = (numbers, res = []) => numbers ? (numbers.forEach((v, i) => res.push((v + numbers[i - 1]) / 2)), res).slice(1) : []



q = averages([2, 2, 2, 2, 2]) // [2, 2, 2, 2]
q
q = averages([2, -2, 2, -2, 2]) // [0, 0, 0, 0]
q
q = averages([1, 3, 5, 1, -10]) // [2, 4, 3, -4.5]
q