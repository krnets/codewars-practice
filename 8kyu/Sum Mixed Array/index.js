// 8kyu - Sum Mixed Array

const sumMix = x => x.reduce((a, b) => a + Number(b), 0)

// const sumMix = x => eval(x.join('+'))

q = sumMix([9, 3, '7', '3']) // 22
q
q = sumMix(['5', '0', 9, 3, 2, 1, '9', 6, 7]) // 42
q
q = sumMix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']) // 41
q