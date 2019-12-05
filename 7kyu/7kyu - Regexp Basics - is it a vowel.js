// 7kyu - Regexp Basics - is it a vowel?

/* Implement String#vowel? (in Java StringUtils.isVowel(String)), 
which should return true if given object is a vowel, false otherwise. */

String.prototype.vowel = function () {
    return /^[aeiou]$/i.test(this)
}

q = ''.vowel() // false
q
q = 'a'.vowel() // true
q
q = 'E'.vowel() // true
q
q = 'ou'.vowel() // false
q
q = 'z'.vowel() // false
q
q = 'lol'.vowel() // false
q