/* V A P O R C O D E  [7]
Write a function that converts any sentence into a V A P O R W A V E sentence. 
a V A P O R W A V E sentence converts all the letters into uppercase, 
and adds 2 spaces between each letter (or special character) to create this 
V A P O R W A V E effect. */

// function vaporcode(string) {
//     return string.toUpperCase().split(' ').join('').split('').join(' ')
// }

function vaporcode(string) {
    // return string.toUpperCase().match(/[^ ]/g).join `  `
    let a = string.toUpperCase()
    a
    let b = a.match(/[^ ]/g)
    b
    let c = b.join(' ')
    c
    return c
}

q = vaporcode("Lets go to the movies") // output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
q
// q = vaporcode("Why isn't my code working?") // output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
// q