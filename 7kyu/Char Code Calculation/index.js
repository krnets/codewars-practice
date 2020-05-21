// 7kyu - Char Code Calculation

/* Given a string, turn each letter into its ASCII character code and join them together to create a number - 
let's call this number total1:

'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667

Then replace any incidence of the number 7 with the number 1, and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^

Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6   */

// function calc(x) {
//     let total1 = [...x].map(v => v.charCodeAt()).join('')
//     let total2 = total1.replace(/7/g, 1)
//     return [...total1].reduce((a, b) => a + Number(b), 0) - [...total2].reduce((a, b) => a + Number(b), 0)
// }

// const calc = x => (x.replace(/./g, c => c.charCodeAt()).match(/7/g) || []).length * 6

const calc = s => [...s].map(c => c.charCodeAt()).toString().replace(/[^7]/g, '').length * 6

q = calc('ABC') // 6
q
q = calc('abcdef') // 6
q
q = calc('ifkhchlhfd') // 6
q
q = calc('aaaaaddddr') // 30
q
q = calc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') // 96
q