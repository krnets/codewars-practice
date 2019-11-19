// 6kyu - Highest Scoring Word

// function high(x) {
//     let alphabet = 'abcdefghijklmnopqrstuvwxyz'
//     let a = x.split(' ')
//     let b = a.map(v => v.split('').reduce((acc, curr) => acc + (alphabet.indexOf(curr) + 1), 0))
//     let c = [...b].sort((x,y) => y - x)[0]
//     let d = b.indexOf(c)
//     return a[d]
// }

// function high(x) {
//     let alphabet = 'abcdefghijklmnopqrstuvwxyz'
//     let a = x.split(' ')
//     let b = a.map(v => v.split('').reduce((t, c) => t + (alphabet.indexOf(c) + 1), 0))
//     let c = [...b].sort((x, y) => y - x)[0]
//     return a[b.indexOf(c)]
// }

function high(x) {
    let alpha = 'abcdefghijklmnopqrstuvwxyz'
    let words = x.split(' ')
    let score = words.map(v => v.split('').reduce((t, c) => t + (alpha.indexOf(c) + 1), 0))

    return words[score.indexOf(Math.max(...score))]
}

q = high('man i need a taxi up to ubud') // 'taxi'
q
q = high('what time are we climbing up the volcano') // 'volcano'
q
q = high('take me to semynak') // 'semynak'
q