// function arrayLeaders(numbers) {
//     let leaders = []
//     let tail, sum
//     for (let i = 0; i < numbers.length; i++) {
//         tail = numbers.slice(i + 1, numbers.length)
//         sum = tail.reduce((a, b) => a + b, 0)
//         if (numbers[i] > sum) {
//             leaders.push(numbers[i])
//         }
//     }
//     return leaders
// }

const arrayLeaders = numbers => numbers
            .filter((value, index) => numbers.slice(index + 1)
                                             .reduce((sum, b) => sum + b, 0) 
                                             < value)

q = arrayLeaders([1, 2, 3, 4, 0]) // [4]
q
q = arrayLeaders([16, 17, 4, 3, 5, 2]) // [17,5,2]
q
q = arrayLeaders([-1, -29, -26, -2]) // [-1]
q
q = arrayLeaders([-36, -12, -27]) //  [-36,-12]
q
q = arrayLeaders([5, -2, 2]) // [5,2]
q
q = arrayLeaders([0, -1, -29, 3, 2]) //  [0,-1,3,2]
q



