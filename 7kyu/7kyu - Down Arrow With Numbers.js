// 7kyu - Down Arrow With Numbers

/* Given a number n, make a down arrow shaped pattern.

For example, when n = 5, the output would be:

123454321
 1234321
  12321
   121
    1

and for n = 11, it would be:

123456789010987654321
 1234567890987654321
  12345678987654321
   123456787654321
    1234567654321
     12345654321
      123454321
       1234321
        12321
         121
          1

An important thing to note in the above example is that the numbers greater than 9 still stay single digit, 
like after 9 it would be 0 - 9 again instead of 10 - 19.

Note: There are spaces for the indentation on the left of each line and no spaces on the right. */

// function getADownArrowOf(n) {
//     let init10 = [...Array(10).keys()]
//     let arrange = init10.slice(1).concat(init10.slice(0, 1))
//     let multiply = Array(Math.abs(Math.floor(n))).fill(arrange).reduce((x, y) => x.concat(y), [])
//     let increasing = multiply.slice(0, n)
//     let decreasing = increasing.slice().reverse().slice(1)
//     let combined = increasing.concat(decreasing)
//     let res = []
//     for (let i = n, j = 0; i > 0; i--, j++)
//         res.push(' '.repeat(j) + combined.slice(0, i).concat(decreasing.slice(j)).join(''))
//     return res.join('\n')
// }

function getADownArrowOf(n) {
    let rows = []
    let nums = '1234567890'
    for (let i = n; i > 0; i--) {
        let row = nums.repeat((i / 10) + 1).slice(0, i)
        row += [...row.slice(0, row.length - 1)].reverse().join('')
        rows.push(' '.repeat(n - i) + row)
    }
    return rows.join('\n')
}

q = getADownArrowOf(1) // "1"
q
q = getADownArrowOf(3) // "12321\n 121\n  1"
q
q = getADownArrowOf(5) // "123454321\n 1234321\n  12321\n   121\n    1"
q