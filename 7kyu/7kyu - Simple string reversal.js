// 7kyu - Simple string reversal

/* In this Kata, we are going to reverse a string while maintaining spaces.

-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo" */

// spc.includes(i) ? out += ' ' : out += rev.pop()

// function solve(str) {
//     let rev = [...str.split(' ').join('')]
//     let spc = [...str].reduce((acc, v, i) => v == ' ' ? acc.concat(i) : acc, [])
//     for (var out = '', i = 0; i < str.length; i++)
//         out += (spc.includes(i) ? ' ' : rev.pop())
//     return out
// }

function solve(str) {
    let arr = [...str].filter(v => v != ' ')
    return str.replace(/\S/g, _ => arr.pop())
}

q = solve("codewars") // "srawedoc"
q
q = solve("your code") // "edoc ruoy"
q
q = solve("your code rocks") // "skco redo cruoy"
q
q = solve("i love codewars") // "s rawe docevoli"
q