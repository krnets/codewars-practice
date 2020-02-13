// 7kyu - Nickname Generator

/* Write a function, nicknameGenerator that takes a string name as an argument and 
returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"

If the 3rd letter is a vowel, return the first 4 letters.

nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"

If the string is less than 4 characters, return "Error: Name too short".

    Vowels are "aeiou", so discount the letter "y".
    Input will always be a string.
    Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
    The input can be modified */

// const nicknameGenerator = name =>
//     name.length <= 3 ? 'Error: Name too short' : /[aeiou]/.test(name[2]) ? name.slice(0, 4) : name.slice(0, 3)

const nicknameGenerator = name => name.length > 3 ? name.slice(0, 3 + /[aeiou]/.test(name[2])) : 'Error: Name too short'

q = nicknameGenerator('Jimmy') // "Jim"
q
q = nicknameGenerator('Samantha') // "Sam"
q
q = nicknameGenerator('Sam') // "Error: Name too short"
q
q = nicknameGenerator('Kayne') // "Kay", "'y' is not a vowel"
q
q = nicknameGenerator('Melissa') // "Mel"
q
q = nicknameGenerator('James') // "Jam"
q
