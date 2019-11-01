// function divisibleBy(numbers, divisor){
//     return numbers.filter(x => x % divisor === 0)
//     // return output;
// }
const divisibleBy = (numbers, divisor) => numbers.filter(x => x % divisor == 0)

q = divisibleBy([1, 2, 3, 4, 5, 6], 2)
q
// , [2,4,6]);

q = divisibleBy([1, 2, 3, 4, 5, 6], 3)
q
//  [3,6])

q = divisibleBy([0, 1, 2, 3, 4, 5, 6], 4)
//  [0,4])
q

q = divisibleBy([0], 4)
//  [0])
q

q = divisibleBy([1, 3, 5], 2)
//  [])
q