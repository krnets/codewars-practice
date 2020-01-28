// 7kyu - Hungarian Vowel Harmony (easy)

/* Vowel harmony is a phenomenon in some languages. 
It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")" 
 This kata is based on vowel harmony in Hungarian.

Your goal is to create a function dative() which returns the valid form of a valid Hungarian word w in dative case 
i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

Vowel Harmony Rules (simplified)
When the last vowel in the word is

    a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
    a back vowel (a, á, o, ó, u, ú) the suffix is -nak

    To keep it simple: All words end with a consonant
    All strings are unicode strings.
    There are no grammatical exceptions in the tests. */

// function dative(word) {
//     let backVowel = "aáoóuú"
//     let str = word.replace(/[bcdfghjklmnpqrstvwxyz]/g, '')
//     return backVowel.includes(str[str.length - 1]) ? word + 'nak' : word + 'nek'
// }

const dative = (word) => /[eéiíöőüű][^aáoóuú]*$/.test(word) ? word + 'nek' : word + 'nak'

q = dative("ablak") // "ablaknak"
q
q = dative("tükör") // "tükörnek"
q
q = dative("keret") // "keretnek"
q
q = dative("otthon") // "otthonnak"
q
q = dative("virág") // "virágnak"
q
q = dative("tett") // "tettnek"
q
q = dative("rokkant") // "rokkantnak"
q
q = dative("rossz") // "rossznak"
q
q = dative("gonosz") // "gonosznak"
q