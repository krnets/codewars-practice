// 6kyu - Stop gninnipS My sdroW!

// function spinWords() {
//     let words = [...arguments][0].split(' ')
//     return words.map(v => v.length > 4 ? [...v].reverse().join `` : v).join ` `
// }

// const spinWords = words => words.split(' ').map(v => v.length > 4 ? v.split('').reverse().join('') : v).join(' ')
// const spinWords = words => words.replace(/\w{5,}/g, w => w.split('').reverse().join(''))
const spinWords = words => words.replace(/\w{5,}/g, w => w.split ``.reverse().join ``)

q = spinWords("Welcome") // "emocleW"
q
q = spinWords("Hey fellow warriors") // "Hey wollef sroirraw"
q
q = spinWords("This is a test") // "This is a test"
q
q = spinWords("This is another test") // "This is rehtona test"
q
q = spinWords("You are almost to the last test") // "You are tsomla to the last test"
q
q = spinWords("Just kidding there is still one more") // "Just gniddik ereht is llits one more"
q
q = spinWords("Seriously this is the last one") // "ylsuoireS this is the last one"
q