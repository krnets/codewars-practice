// 6kyu - Vowel Shifting

/* You get a "text" and have to shift the vowels by "n" positions to the right.
(Negative value for n should shift to the left.)
"Position" means the vowel's position if taken as one item in a list of all vowels within the string.
A shift by 1 would mean, that every vowel shifts to the place of the next vowel.

Shifting over the edges of the text should continue at the other edge.

text = "This is a test!"
n = 1
output = "Thes is i tast!"

text = "This is a test!"
n = 3
output = "This as e tist!"

If text is null or empty return exactly this value. */


// function vowelShift(text, n) {
//     let vowelsFound = text.match(/[aeiou]/gi)
//     let vowelIndices = [...text].map((v, i) => /[aeiou]/i.test(v) ? i : null)
//     let rotateLeft = (arr, n) => arr.map((v, i) => arr[(i + n) % arr.length])
//     let rotateRight = (arr, n) => arr.map((v, i) => (i - n) % arr.length < 0 ? arr[arr.length + (i - n) % arr.length] : arr[(i - n) % arr.length])
//     // return rotateRight(vowelsFound, 1)
//     // return rotateLeft(vowelsFound, 1)
//     // return vowelsFound
//     let vowelsRotatedRight = rotateRight(vowelsFound, n)
//     // let vowelsRotatedLeft = rotateLeft(vowelsFound, 0)
//     // return vowelIndices
//     // return vowelsRotatedRight
//     // return vowelsRotatedLeft
//     return [...text].map((v,i) => vowelIndices[i] == i ? vowelsRotatedRight.shift() : v).join('')
//     // return [...text].map((v,i) => vowelIndices[i] == i ? vowelsRotatedLeft.shift() : v)
// }

// function vowelShift(text, n) {
//     if (!text) return text
//     let vow = text.match(/[aeiou]/gi) || []
//     let idx = [...text].map((v, i) => /[aeiou]/i.test(v) ? i : null)
//     let rot = vow.map((v, i) => (i - n) % vow.length < 0 ? vow[vow.length + (i - n) % vow.length] : vow[(i - n) % vow.length])
//     return [...text].map((v, i) => idx[i] == i ? rot.shift() : v).join('')
// }

function vowelShift(text, n) {
    if (!text) return text
    let vow = text.match(/[aeiou]/gi) || []
    vow = vow.slice(-n % vow.length).concat(vow.slice(0, -n % vow.length))
    return text.replace(/[aeiou]/gi, _ => vow.shift())
}

// Basic Tests
q = vowelShift("This is a test!", 0) // "This is a test!"
q
q = vowelShift("This is a test!", 1) // "Thes is i tast!"
q
q = vowelShift("This is a test!", 3) // "This as e tist!"
q