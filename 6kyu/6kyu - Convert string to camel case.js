// 6kyu - Convert string to camel case

/* Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).  */

// function toCamelCase(str) {
//     if (str == '') return str
//     let res = str.split(/\-|\_/).map(v => v[0].toUpperCase() + v.slice(1)).join ``
//     return str[0] == str[0].toUpperCase() ? res : res[0].toLowerCase() + res.slice(1)
// }

const toCamelCase = str => str.replace(/[_-]\w/gi, ch => ch[1].toUpperCase())
// const toCamelCase = str => str.replace(/[^a-z]./gi, x => x.toUpperCase().slice(-1))

q = toCamelCase('') // ''
q
q = toCamelCase("the_stealth_warrior") // "theStealthWarrior"
q
q = toCamelCase("The-Stealth-Warrior") // "TheStealthWarrior"
q
q = toCamelCase("A-B-C") // "ABC"
q