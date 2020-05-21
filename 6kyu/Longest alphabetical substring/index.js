// 6kyu - Longest alphabetical substring

/* Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.
The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first. */

// function longest(str) {
//     let max = ''
//     let res = [...str].reduce((sub, c) => (c >= sub.slice(-1) ? sub + c : (max = sub.length > max.length ? sub : max, c)), '')
//     return res.length > max.length ? res : max
// }

// const longest = str => str.match(/a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*/g).reduce((a, b) => a.length >= b.length ? a : b);

// function longest(str) {
//     let abc = new RegExp('a'.repeat(26).replace(/./g, (_, i) => String.fromCharCode(i + 97) + '*'), 'g')
//     return str.match(abc).reduce((a, b) => a.length >= b.length ? a : b)
// }

// const longest = (str) => str.match(new RegExp('a'.repeat(26).replace(/./g, (_, i) => String.fromCharCode(i + 97) + '*'), 'g')).reduce((a, b) => a.length <= b.length ? b : a)

function longest(str) {
    [pos, current, max] = [0, 0, 0]
    for (let i = 1; i < str.length; i++) {
        if (str[i - 1] <= str[i]) {
            current++
            if (current > max) {
                max = current
                pos = i - max
            }
        } else current = 0
    }
    return str.slice(pos, pos + max + 1)
}

q = longest('') // [empty string]
q
q = longest('asd') // 'as'
q
q = longest('nab') // 'ab'
q
q = longest('abcdeapbcdef') // 'abcde'
q
q = longest('asdfaaaabbbbcttavvfffffdf') // 'aaaabbbbctt'
q
q = longest('asdfbyfgiklag') // 'fgikl'
q
q = longest('z') // 'z'
q
q = longest('zyba') // 'z'
q