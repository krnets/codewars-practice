// 6kyu - Character frequency

function letterFrequency(text) {
    let count = {};
    let lettersOnly = text.replace(/[^a-z]\s*/gi, '').toLowerCase();

    [...lettersOnly].forEach(c => count[c] = (count[c] || 0) + 1)

    let array = Object.keys(count).map(v => [v, count[v]])
    return array.sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
}

// function letterFrequency(text) {
//     return (text
//             .replace(/[^a-z]\s*/gi, '')
//             .toLowerCase()
//             .split('')
//             .sort()
//             .join('')
//             .match(/(\w)\1+|(\w)/g) || [])
//         .map(v => [v[0], v.length])
//         .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
// }

// const _ = require('lodash')

// function letterFrequency(text) {
//     return _(text.toLowerCase()).filter(c => 'a' <= c && c <= 'z').countBy().toPairs().sortBy([p => -p[1], p => p[0]]).value()
// }



// q = letterFrequency('wklv lv d vhfuhw phvvdjh')
// // expected = [['v', 5], ['h', 4], ['d', 2], ['l', 2], ['w', 2], ['f', 1], ['j', 1], ['k', 1], ['p', 1], ['u', 1]]
// q

q = letterFrequency("As long as I'm learning something, I figure I'm OK - it's a decent day.")
// expected = [["i", 7], ["a", 5], ["e", 5], ["n", 5], ["g", 4], ["s", 4], ["m", 3], ["o", 3], ["t", 3], ["d", 2], ["l", 2], ["r", 2], ["c", 1], ["f", 1], ["h", 1], ["k", 1], ["u", 1], ["y", 1]]
q

// q = letterFrequency('IWT LDGAS XH HIXAA P LTXGS EAPRT, STHEXIT BN TUUDGIH ID BPZT RATPG PCS ETGUTRI HTCHT DU XI.')
// // expected = [["t", 12], ["i", 7], ["h", 6], ["a", 5], ["g", 5], ["p", 5], ["x", 5], ["d", 4], ["s", 4], ["u", 4], ["e", 3], ["r", 3], ["b", 2], ["c", 2], ["l", 2], ["n", 1], ["w", 1], ["z", 1]]
// q