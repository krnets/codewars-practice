// 6kyu - Counting Duplicates

function duplicateCount(text) {
    let count = {}
    if (!text) return 0;
    [...text.toLowerCase()].forEach(v => count[v] = (count[v] || 0) + 1)

    return Object.values(count).filter(v => v > 1).length
}

// const duplicateCount = text => (text.toLowerCase().split('').sort().join('').match(/([^])\1+/g) || []).length
// const duplicateCount = text => ([...text.toLowerCase()].sort().join ``.match(/([^])\1+/g) || []).length

// const duplicateCount = text => [...text.toLowerCase()].filter((v, i, a) => a.indexOf(v) != i && a.lastIndexOf(v) == i).length

// const duplicateCount = text => [...text.toLowerCase()].reduce((a, l) => { a[l] = (a[l] || 0) + 1;
//                                 if (a[l] == 2) a.count++; return a; }, { count: 0 }).count

// function duplicateCount(text) {
//     let count = 0
//     let letters = []
//     let s = text.toLowerCase();

//     [...s].forEach(letter => {
//         if (!letters.includes(letter) && (s.split(letter).length - 1) > 1) {
//             letters.push(letter)
//             count++
//         }
//     })
//     return count
// }


q = duplicateCount("") // 0
q
q = duplicateCount("abcde") // 0
q
q = duplicateCount("aabbcde") // 2
q
q = duplicateCount("aabBcde") // 2
q
q = duplicateCount("Indivisibility") // 1
q
q = duplicateCount("Indivisibilities") // 2
q