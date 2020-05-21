// 7kyu - Alternating between three values

// function f(x, cc) {
//     let vals = Object.values(cc)
//     let c = vals.indexOf(x)
    
//     return vals[c+1] == undefined ? vals[0] : vals[c+1]
// }

function f(x, cc) {
    let vals = Object.values(cc)
    return vals[(vals.indexOf(x) + 1) % vals.length]
}

q = f(3, {a: 3, b: 4, c: 5}) // 4
q
q = f(4, {a: 3, b: 4, c: 5}) // 5
q
q = f(5, {a: 3, b: 4, c: 5}) // 3
q