// 6kyu - Simple Fun #369: Count Binary Substring I


// function count(s1, s2) {
//     let count = 0
//     for (let i = 0; i < s2.length - s1.length + 1; i++)
//         if (s1 == s2.slice(i, i + s1.length))
//             count++
//     return count
// }

// function count(s1, s2) {
//     let arr = []
//     for (let i = 0; i < s2.length - s1.length + 1; i++)
//         arr.push(s2.slice(i, i + s1.length))
//     return arr.filter(v => v == s1).length
// }

function count(s1, s2) {
    let res = pos = 0;
    while (pos = s2.indexOf(s1, pos) + 1)
        res++
    return res
}

// function count(s1, s2) {
//     let res = 0
//     let pos = -1
//     while ((pos = s2.indexOf(s1, pos + 1)) != -1)
//         res++
//     return res
// }

// function count(s1, s2) {
//     var count = 0,
//         i = s2.indexOf(s1)
//     while (i < s2.length) {
//         if (i < 0) return count
//         count++
//         i = s2.indexOf(s1, i + 1)
//     }
//     return count
// }

// function count(s1, s2) {
//     var count = 0;
//     if (s2.indexOf(s1) !== -1) {
//         for (var i = 0; i < s2.length; i++) {
//             if (s2.slice(i, i + s1.length).indexOf(s1) !== -1) {
//                 ++count;
//             }
//         }
//     }
//     return count;
// }

// function count(s1, s2) {
//     var count = 0;
//     for (var i = 0; i < s2.length; i++) {
//         var str = s2.slice(i, i + s1.length)
//         if (s1 == str) {
//             count++;
//         }
//     }
//     return count;
// }

// function count(s1, s2) {
//     let count = 0
//     let index
//     while ((index = s2.search(s1)) != -1) {
//         s2 = s2.slice(index + 1)
//         count++
//     }
//     return count
// }

// const count = (s1, s2) => (s2.match(new RegExp(`(?=${s1})`, 'g')) || []).length

q = count("11", "1001110110") // 3
q
q = count("101", "110010010010001") // 0
q
q = count("1010", "110100010101011") // 3
q
q = count("0000", "1000000001") // 5
q