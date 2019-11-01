/* Codewars 7 kyu - Alphabetical Addition 
*****************************************
Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being a letter to add.
Notes:
    Letters will always be lowercase.
    Letters can overflow (see second to last example of the description)
    If no letters are given, the function should return 'z'
Examples:
    addLetters('a', 'b', 'c') = 'f'
    addLetters('a', 'b') = 'c'
    addLetters('z') = 'z'
    addLetters('z', 'a') = 'a'
    addLetters('y', 'c', 'b') = 'd' // notice the letters overflowing
    addLetters() = 'z'
******************************************************************************************/

function addLetters(...letters) {
    let s = letters
            .reduce((a,b) => a.concat(b),[])
            .toString().split(',').join('')
    let sum = 0
    for (let i = 0; i < s.length; i++) {
        sum += (s.charCodeAt(i) - 96) 
    }
    sum = (sum % 26 || 26) + 96
    return String.fromCharCode(sum)
}

// q = addLetters(['a','b']) // c
// q
// q = addLetters(['z']) // z
// q
// q = addLetters(['y','c','b']) // d
// q
q = addLetters([]) // z
q