// function betweenExtremes(numbers) {
//     numbers.sort((a, b) => a - b)
//     return numbers.pop() - numbers.shift()
// }


const betweenExtremes = (numbers) => Math.max(...numbers) - Math.min(...numbers)


q = betweenExtremes([21, 34, 54, 43, 26, 12]) // 42
q
q = betweenExtremes([-1, -41, -77, -100]) // 99
q