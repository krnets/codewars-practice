// 6kyu - Find the missing letter

// function findMissingLetter(array) {
//     let firstChar = array.slice(0, 1)
//     let firstCharCode = firstChar[0].charCodeAt()

//     let lastChar = array.slice(-1)
//     let lastCharCode = lastChar[0].charCodeAt()

//     let newArray = Array.from({
//         length: lastCharCode - firstCharCode + 1
//     }, (_, i) => String.fromCharCode(firstCharCode + i))

//     return newArray.filter(v => !array.includes(v)).toString()
// }

function findMissingLetter(array) {
    let first = array[0].charCodeAt()
    let last = array[array.length - 1].charCodeAt()

    return Array.from({
            length: last - first + 1
        }, (_, i) => String.fromCharCode(first + i))
        .filter(v => !array.includes(v)).toString()
}

// function findMissingLetter(letters) {
//     for (let i = 0; i < letters.length; i++)
//         if (letters[i].charCodeAt() + 1 !== letters[i + 1].charCodeAt())
//             return String.fromCharCode(letters[i].charCodeAt() + 1)
// }

// function findMissingLetter(array) {
//     for (i = 1; i < array.length; ++i)
//         if (array[i].charCodeAt() - 1 != array[i - 1].charCodeAt())
//             return String.fromCharCode(array[i].charCodeAt() - 1);
// }

// const findMissingLetter = array => String.fromCharCode(array.reduce((l, v, i) => i == 0 || (l.charCodeAt() + 1 == v.charCodeAt()) ? v : l, '').charCodeAt() + 1)
// const findMissingLetter = array => String.fromCharCode(array.map(ch => ch.charCodeAt()).find((code, i, arr) => i > 0 && code != arr[i - 1] + 1) - 1)

q = findMissingLetter(['a', 'b', 'c', 'd', 'f']) // 'e'
q
q = findMissingLetter(['O', 'Q', 'R', 'S']) // 'P'
q