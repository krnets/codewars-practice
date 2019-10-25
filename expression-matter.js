// const expressionMatter = (a, b, c) => Math.max((a + b + c), (a * b * c), (a * (b + c)))

// function expressionMatter() {
//     let result = arguments[0] > arguments[2] ? [...arguments].reverse() : [...arguments];
//     return result.reduce((x,y)=>x < 2 || y < 2 ? x + y : x * y);
//   }

q = expressionMatter(2, 1, 2) // 6
q
q = expressionMatter(2, 1, 1) // 4
q
q = expressionMatter(1, 1, 1) // 3
q
q = expressionMatter(1, 2, 3) // 9
q
q = expressionMatter(1, 3, 1) // 5
q
q = expressionMatter(2, 2, 2) // 8
q
q = expressionMatter(5, 1, 3) // 20
q
q = expressionMatter(3, 5, 7) //105
q
q = expressionMatter(5, 6, 1) // 35
q
q = expressionMatter(1, 6, 1) // 8
q
q = expressionMatter(2, 6, 1) // 14
q
q = expressionMatter(6, 7, 1) // 48
q
q = expressionMatter(2, 10, 3) // 60
q
q = expressionMatter(1, 8, 3) // 27
q
q = expressionMatter(9, 7, 2) //126
q
q = expressionMatter(1, 1, 10) // 20
q
q = expressionMatter(9, 1, 1) // 18
q
q = expressionMatter(10, 5, 6) //300
q
q = expressionMatter(1, 10, 1) // 12
q
