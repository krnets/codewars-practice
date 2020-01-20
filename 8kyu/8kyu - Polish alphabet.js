// 8kyu - Polish alphabet

/* There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
Your task is to change the letters with diacritics:

ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z

and print out the string without the use of the Polish letters.

Input: "Jędrzej Błądziński"
Output: "Jedrzej Bladzinski" */


// return string.split('').map(v => v.toUpperCase() == v && v.toLowerCase())

// function correctPolishLetters(string) {
//     let diacritics = 'ąćęłńóśźż'
//     let fromDiacritics = {ą:'a',ć:'c',ę:'e',ł:'l',ń:'n',ó:'o',ś:'s',ź:'z',ż:'z'}
//     let res = ''
//     for (let i = 0; i < string.length; i++) {
//         let cmp = string[i].toLowerCase()
//         if(diacritics.includes(cmp)) 
//             res += fromDiacritics[cmp]
//         else res += string[i]
//     }
//     return res
// }

// function correctPolishLetters(string) {
//     let diacritics =  {ą:'a',ć:'c',ę:'e',ł:'l',ń:'n',ó:'o',ś:'s',ź:'z',ż:'z'}
//     return string.replace(/[ąćęłńóśźż]/g, match => diacritics[match])
// }

const correctPolishLetters = (string) => string.replace(/[ąćęłńóśźż]/g, c => 'acelnoszz' ['ąćęłńóśźż'.indexOf(c)])

// const correctPolishLetters = string => string.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ł/g, 'l');


q = correctPolishLetters("Jędrzej Błądziński") // "Jedrzej Bladzinski"
q
q = correctPolishLetters("Lech Wałęsa") // "Lech Walesa"
q
q = correctPolishLetters("Maria Skłodowska-Curie") // "Maria Sklodowska-Curie"
q