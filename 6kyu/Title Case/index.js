// 6kyu - Title Case

// function titleCase (title, minorWords)  {
//     if (title == '') 
//         return ''

//     let a = title.toLowerCase()
//     a 

//     let mw = minorWords ? minorWords.split(' ').map(v => v.toLowerCase()) : []
//     mw

//     let b = a.split(' ')
//     b

//     let c = b.map(v => (String.fromCharCode(v.charCodeAt() - 32)) + v.slice(1))
//     c

//     let d = c.map((word,i) => mw.includes(word.toLowerCase()) ? word.toLowerCase() : word)
//     d

//     let e = d.join(' ')
//     e

//     let f = e[0].toUpperCase() + e.slice(1)
//     f

//     return f
// }

// let b = a.split(' ')
// let c = b.map(v => (String.fromCharCode(v.charCodeAt() - 32)) + v.slice(1))
// let d = c.map((word,i) => mw.includes(word.toLowerCase()) ? word.toLowerCase() : word)
// let e = d.join(' ')

function titleCase(title, minorWords) {
    if (title == '') return ''

    let mw = minorWords ? minorWords.split(' ').map(v => v.toLowerCase()) : []
    let a = title.toLowerCase()
    let b = a.split(' ').map(v => (String.fromCharCode(v.charCodeAt() - 32)) + v.slice(1))
    let c = b.map((word, i) => mw.includes(word.toLowerCase()) ? word.toLowerCase() : word).join(' ')

    return c[0].toUpperCase() + c.slice(1)
}

q = titleCase('') // ''
q
q = titleCase('a clash of KINGS', 'a an the of') // 'A Clash of Kings'
q
q = titleCase('THE WIND IN THE WILLOWS', 'The In') // 'The Wind in the Willows'
q
q = titleCase('the quick brown fox') // 'The Quick Brown Fox'
q