// 6kyu - Grouped by commas

/* Finish the solution so that it takes an input n (integer) and returns a string that is the 
decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647
Examples

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"

Algorithms | String Formatting | Formatting | Strings | Numbers */

// function groupByCommas(n) {
//     let res = []
//     let arr = [...String(n)]
//     for (let i = 0; i < arr.length; i++)
//         res.push(arr.splice(-3).join(''))
//     res.push(arr.join(''))
//     return res.reverse().join(',').replace(/^\,/, '')
// }

// const groupByCommas = (n) => n.toLocaleString('en')
const groupByCommas = (n) => String(n).split(/(?=(?:\d{3})+$)/).join(',')
// const groupByCommas = (n) => String(n).replace(/(\d)(?=(\d{3})+$)/g, '$1,')
// const groupByCommas = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ',')
// const groupByCommas = (n) => String(n).replace(/(?<=\d)(?=(\d{3})+(?!\d))/g, ',')

q = groupByCommas(1) // '1'
q
q = groupByCommas(10) // '10'
q
q = groupByCommas(100) // '100'
q
q = groupByCommas(1000) // '1,000'
q
q = groupByCommas(10000) // '10,000'
q
q = groupByCommas(100000) // '100,000'
q
q = groupByCommas(1000000) // '1,000,000'
q
q = groupByCommas(35235235) // '35,235,235'
q