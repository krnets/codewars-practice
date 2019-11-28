// 7kyu - String Matcher

/* isMatching checks if a string can be created by combining and rearranging the letters of two other strings (not case sensitive).
!Spaces will be ignored but special characters and numbers won't match the string and return false.

isMatching("email box", "b aIl", "Mo x e") return true
but
isMatching("bouh", "0b", "uh") return false

You need to be able to use all the caracters from the two strings so:
isMatching("kata", "kt", "aaa") return false */

function isMatching(string, str1, str2) {
    let a = [...string.replace(/\s+/g, '').toLowerCase()]
    let b = [...str1.concat(str2).replace(/\s+/g, '').toLowerCase()]
    return a.every(v => b.includes(v)) && a.length == b.length
}

q = isMatching("bouh", "0", "buh") // false
q
q = isMatching("kitten", "t", "eink") // false
q
q = isMatching("mentalist", "l.st", "metan") // false
q
q = isMatching("impressionistic", "isis isi", "precomnt") // true
q
q = isMatching("email box", "bail", "moxe") // true
q
q = isMatching("detail", "tlei", "dai") // false
q