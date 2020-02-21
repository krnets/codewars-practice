// 7kyu - Make acronym

/* Write function toAcronym which takes a string and make an acronym of it.

Rule of making acronym in this kata:

    split string to words by space char
    take every first letter from word in given string
    uppercase it
    join them toghether

Code wars -> C, w -> C W -> CW */

// const toAcronym = input => input.split(' ').map(v => v[0]).join('').toUpperCase()

// const toAcronym = input => input.replace(/(\w).*?\b[^\w]*/g, '$1').toUpperCase()

const toAcronym = input => input.match(/(?=\b)(\w)/g).join('').toUpperCase()

q = toAcronym("Code Wars") // "CW"
q
q = toAcronym("Water Closet") // "WC"
q
q = toAcronym("Portable Network Graphics") // "PNG"
q
q = toAcronym("PHP: Hypertext Preprocessor") // "PHP"
q
q = toAcronym("hyper text markup language") // "HTML"
q