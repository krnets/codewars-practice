// 7kyu - Replace every nth

/* Write a method, that replaces every nth char oldValue with char newValue.

replaceNth(text, n, oldValue, newValue)

n:         2
oldValue: 'a'
newValue: 'o'
"Vader said: No, I am your father!" -> "Vader soid: No, I am your fother!"
  1     2          3        4       -> 2nd and 4th occurence are replaced

Your method has to be case sensitive!
As you can see in the example: The first changed is the 2nd 'a'. 
So the start is always at the nth suitable char and not at the first!
If n is 0 or negative or if it is larger than the count of the oldValue, return the original text without a change.
The text and the chars will never be null. */

// function replaceNth(text, n, oldValue, newValue) {
//     if (n <= 0 || n > oldValue) return text
//     let res = [...text]
//     for (let i = 0, trackValue = 0; i < res.length; i++) {
//         if (res[i] == oldValue) {
//             trackValue++
//         }
//         if (trackValue == n) {
//             res[i] = newValue
//             trackValue = 0
//         }
//     }
//     return res.join('')
// }


const replaceNth = (text, n, oldValue, newValue) => n < 1 ? text : 
    [...text].reduce((acc, v) => ((v == oldValue && ++acc.ch % n == 0) ? acc.str += newValue : acc.str += v, acc), {str: '', ch: 0}).str

// const replaceNth = (text, n, oldValue, newValue, i = 1) => n < 1 ? text : text.replace(RegExp(oldValue, "g"), _ => i++ % n ? oldValue : newValue)

// const replaceNth = (text, n, a, b, c = 0) => text.split('').map(e => e === a ? ++c === n ? (c = 0) ? b : b : e : e).join('');


q = replaceNth("Vader said: No, I am your father!", 2, 'a', 'o') // "Vader soid: No, I am your fother!"
q
q = replaceNth("Vader said: No, I am your father!", 4, 'a', 'o') // "Vader said: No, I am your fother!"
q
q = replaceNth("Vader said: No, I am your father!", 6, 'a', 'o') // "Vader said: No, I am your father!"
q
q = replaceNth("Vader said: No, I am your father!", 0, 'a', 'o') // "Vader said: No, I am your father!"
q
q = replaceNth("Vader said: No, I am your father!", -2, 'a', 'o') // "Vader said: No, I am your father!"
q
q = replaceNth("Vader said: No, I am your father!", 1, 'i', 'y') // "Vader sayd: No, I am your father!"
q
q = replaceNth("Luke cries: Noooooooooooooooo!", 6, 'o', 'i') // "Luke cries: Noooooioooooioooo!"
q