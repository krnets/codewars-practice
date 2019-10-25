// function solve(s) {
//     return [...s].map(v => v.toLowerCase() == v).filter(v => v).length >= s.length / 2 ? 
//            [...s].map(v => v.toLowerCase()).join `` : 
//            [...s].map(v => v.toUpperCase()).join ``
// }

function solve(s) {
    return s.replace(/[a-z]/g, '').length > s.length / 2 ?
           s.toUpperCase() :
           s.toLowerCase()
}

// const solve = s => [...s].reduce((t, c) => t + /[a-z]/.test(c) * 2, 0) < s.length ? s.toUpperCase() : s.toLowerCase();

q = solve("code") // "code"
q
q = solve("CODe") // "CODE"
q
q = solve("COde") // "code"
q
q = solve("Code") // "code"
q