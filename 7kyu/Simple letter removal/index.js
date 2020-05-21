// 7kyu - Simple letter removal

/* In this Kata, you will be given a lower case string and your task will be to remove k characters 
from that string using the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first. */

// function solve(s, k) {
//     let chars = [...s].sort().filter((v, i, a) => a.indexOf(v) == i)
//     for (c of chars) {
//         while (s.includes(c)) {
//             if (k == 0 || s == '') break
//             s = s.replace(c, '')
//             k--
//         }
//     }
//     return s
// }

function solve(s, k) {
    let abc = 'a'.repeat(26).replace(/./g, (c, i) => String.fromCharCode(i + 97))
    for (c of abc) {
        while (s.includes(c)) {
            if (k == 0 || s == '') break
            s = s.replace(c, '')
            k--
        }
    }
    return s
}

// function solve(s, k) {
//     let chars = [...s].sort().slice(0, k)
//     for (const c of chars)
//         s = s.replace(c, '')
//     return s
// }

q = solve('abracadabra', 1) // 'bracadabra' # remove the leftmost 'a'.
q
q = solve('abracadabra', 2) // 'brcadabra'  # remove 2 'a' from the left.
q
q = solve('abracadabra', 6) // 'rcdbr'      # remove 5 'a', remove 1 'b'
q
q = solve('abracadabra', 8) // 'rdr'
q
q = solve('abracadabra', 50) // ''
q
