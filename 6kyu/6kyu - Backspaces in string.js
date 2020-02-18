// 6kyu - Backspaces in string

/* Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  "" */

// function cleanString(s) {
//     for (var res = [], i = 0; i < s.length; i++)
//         (s[i] == '#') ? res.pop() : res.push(s[i])
//     return res.join('')
// }

// const cleanString = s => [...s].reduce((r, v) => v == '#' ? r.slice(0, -1) : r + v, '')

function cleanString(s) {
    return [...s].reduce((r, v) => v == '#' ? r.slice(0, -1) : r + v, '')
}

// const cleanString = s => /#/.test(s) ? cleanString(s.replace(/[^#]?#/, '')) : s

// function cleanString(s) {
//     return /#/.test(s) ? cleanString(s.replace(/[^#]?#/, '')) : s
// }


q = cleanString('abc#d##c') // "ac"
q
q = cleanString('abc####d##c#') // "" 
q