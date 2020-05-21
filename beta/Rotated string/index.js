// Beta - Rotated string

// const isRotation = (s1, s2) => {
//     let end = start = 0
//     for (let i = 0, j = s1.length - 1; i < s1.length - 1; i++, j--) {
//         start = s1.slice(0, i + 1)
//         end = s1.slice(-j)
//         if (end + start == s2)
//             return true
//     }
//     return s1 == s2
// }

function isRotation(s1, s2) {
    for (let i = 0; i < s1.length; i++)
        if (s2 == s1.slice(-i) + s1.slice(0, -i))
            return true
    return s1 == s2
}

// const isRotation = (s1, s2) => s1.length == s2.length && (s2 + s2).indexOf(s1) > -1
// const isRotation = (s1, s2) => s1.length == s2.length && (s2 + s2).includes(s1)

q = isRotation('hello', 'ohell') // true
q
q = isRotation('hello', 'lloeh') // false
q
q = isRotation('', '') // true
q