// 7kyu - Sum even numbers

// const sumEvenNumbers = input => input.reduce((acc, v) => v % 2 == 0 ? acc + v : acc, 0)

const sumEvenNumbers = input => eval(input.filter(v => v % 2 == 0).join('+'))

q = sumEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) // 30
q