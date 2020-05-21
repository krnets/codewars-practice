// 7kyu - Greatest Difference

/* Your task is to find the number couple with the greatest difference from a given array of number-couples.
All number couples will be given as strings and all numbers in them will be positive integers.

For instance: ['56-23','1-100']; in this case, you should identify '1-100' as the number couple 
with the greatest difference and return it.

In case there are more than one option, for instance ['1-3','5-7','2-3'], 
you should identify whichever is first, so in this case '1-3'.

If there is no difference, like so ['11-11', '344-344'], return false. */

// function diff(str) {
//     let diff = str.map((v, i) => [Math.abs(eval(v)), i])
//     let max = diff.sort((a, b) => b[0] - a[0])
//     return !diff.every(v => v[0] == max[0][1]) && str[max[0][1]]
// }

// function diff(str) {
//     let arr = str.map(v => Math.abs(eval(v)));
//     let max = Math.max(...arr);
//     return !!max && str[arr.indexOf(max)];
// }

function diff(str) {
    let arr = str.map(v => Math.abs(eval(v)))
    return !(arr.every(v => v == 0)) && str[arr.indexOf(Math.max(...arr))]
}

// const diff = str => str.reduce((m, c) => m[0] < (d = Math.abs(eval(c))) ? [d, c] : m, [0, false])[1]

q = diff(['23-32', '32-23', '2-6', '98-98', '100-101']) // '23-32'
q
q = diff(['22-22', '56-56']) // false
q
q = diff(['52542-522', '0-1000000']) // '0-1000000'
q