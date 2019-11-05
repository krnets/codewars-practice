// function maxGap(numbers) {
//     numbers.sort((a, b) => a - b)
//     let gaps = []
//     let numLength = numbers.length
//     while (numLength > 1) {
//         gaps.push(numbers.splice(-1) - numbers.slice(-1))
//         numLength--
//     }
//     return Math.max.apply(null, gaps)
// }

// const maxGap = numbers => Math.max(...numbers.sort((x, y) => x - y)
//                                              .map((el, i, arr) => i > 0 ? Math.abs(el - arr[i - 1]) : 0));

// function maxGap(numbers) {
//     return numbers
//         .sort((a, b) => a - b)
//         .reduce((max, n, i) => {
//             let gap = numbers[i + 1] - n
//             if (max < gap) {
//                 max = gap
//             }
//             return max
//         }, 0);
// }

// const maxGap = numbers => numbers.sort((a,b) => a - b)
//                                  .reduce((max, curr, i) => {
//                                      let gap = numbers[i+1] - curr 
//                                      if (max < gap)
//                                         max = gap
//                                       return max
//                                  }, 0)



// function maxGap(a, max = 0) {
//     a.sort((a, b) => a - b)
//     for (let i = 1; i < a.length; i++)
//         max = Math.max(max, a[i] - a[i - 1]);
//     return max
// }

const maxGap = (numbers) => numbers.sort((a, b) => a - b)
                                   .reduce((max, curr, i) => numbers[i+1] - curr > max ? 
                                                             numbers[i+1] - curr : max, 
                                                             0)

q = maxGap([13, 10, 2, 9, 5]) // 4
q
q = maxGap([13, 3, 5]) // 8
q
q = maxGap([24, 299, 131, 14, 26, 25]) // 168
q
q = maxGap([-3, -27, -4, -2]) // 23
q
q = maxGap([-7, -42, -809, -14, -12]) // 767
q
q = maxGap([12, -5, -7, 0, 290]) // 278
q
q = maxGap([-54, 37, 0, 64, -15, 640, 0]) // 576
q
q = maxGap([130, 30, 50]) // 80
q
q = maxGap([1, 1, 1]) // 0
q
q = maxGap([-1, -1, -1]) // 0
q