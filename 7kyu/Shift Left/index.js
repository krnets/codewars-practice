// 7kyu - Shift Left

// function shiftLeft(s, t) {
//     const getIndex = (a, b) => {
//         for (let i = 0; i <= a.length; i++)
//             if (b.endsWith(a.slice(i, a.length)))
//                 return i
//     }

//     return getIndex(s, t) + getIndex(t, s)
// }

function shiftLeft(s, t) {
    while (s.slice(-1) === t.slice(-1) && s.length) {
        s = s.slice(0, -1)
        t = t.slice(0, -1)
    }
    return s.length + t.length
}

q = shiftLeft("test", "west") // 2
q
q = shiftLeft("test", "yes") // 7
q
q = shiftLeft("b", "ab") // 1
q