// CHALLENGE 1: REVERSE A STRING
// Return a string in reverse
// ex. reverseString('hello') === 'olleh'

function reverseString(str) {
    // return str
    //     .split('')
    //     .reverse()
    //     .join('')
    ///////////////////////////////////////////////
    // let reversed = ''
    // for (let i = 0; i < str.length; i++) {
    //     console.log(i)    
    //     reversed = reversed + str[i] 
    // }
    ///////////////////////////////////////////////
    // for (let char of str) { 
    //     reversed = reversed + char
    // }
    ///////////////////////////////////////////////

    // str.split('').forEach(char => reversed = char + reversed)
    ///////////////////////////////////////////////
    return str
        .split('')
        .reduce((accumResult, char) => char + accumResult, '')


    // return reversed
}

// Call Function
// q = reverseString('hello')
// q


// CHALLENGE 2: VALIDATE A PALINDROME
// Return true if palindrome and false if not
// ex. isPalindrome('racecar') === 'true', isPalindrome('hello') == false

// const isPalindrome = (str) => reverseString(str) === str
// const isPalindrome = (str) => {
//     return str
//         .split('')
//         .reduce((acc,char) => char + acc, '') === str
// }
const isPalindrome = (str) => {
    return str
        .split('')
        .reverse()
        .join('') === str
}


// q = isPalindrome('racecar')
// q

// CHALLENGE 3: REVERSE AN INTEGER
// Return an integer in reverse
// ex. reverseInt(521) === 125

function reverseInt(input) {
    
    let x = input.toString()
        .split('')
        .reverse()
        .join('')
        
    
    return Math.sign(input) * parseInt(x)
    // return parseInt(x) * Math.sign(input)
}

// q = reverseInt(-521)
// q


// CHALLENGE 4: CAPITALIZE LETTERS
// Return a string with the first letter of every word capitalized
// ex. capitalizeLetters('i love javascript') === 'I Love Javascript'
function capitalizeLetters(str) {

    // let takeFirstLetter = str.split(' ').forEach((v) => v.toUpperCase())
    // return takeFirstLetter
    // let takeFirstLetter = str.split(' ').forEach((v))  
    
    /////////////////////////////////////////////
    // const strArr = str.toLowerCase().split(' ')
    // for (let i = 0; i < strarr.length; i++) {
    //     strarr[i] = strarr[i]
    //                 .substring(0,1)
    //                 .touppercase() 
    //                     +   
    //                 strarr[i]
    //                 .substring(1)
    // }
    ///////////////////////////////////////////////

    // return strArr.join(' ')
    // return str
    //     .split(' ')
    //     .map(word => word[0]
    //         .toUpperCase() + word.substring(1))
    //     .join(' ')
    ///////////////////////////////////////////////
    return str.replace(/\b[a-z]/gi, function(char) {
        return char.toUpperCase()
    })
}

// q = capitalizeLetters('i love javaScript')
// q


// CHALLENGE 5: MAX CHARACTER
// Return the character that is most common in a string
// ex. maxCharacter('javascript') == 'a'
function maxCharacter(str) {
    const charMap = {}
    let maxNum = 0
    let maxChar = ''

    str.split('')
        .forEach(char => {
           char 
           if(charMap[char]) {
               charMap[char]++
           } else {
               charMap[char] = 1
           }
        });

    charMap
    for (let char in charMap) {
       if(charMap[char] > maxNum) {
           maxNum = charMap[char]
           maxChar = char
       }
    }
    return maxChar
}

q = maxCharacter('racetec')
q

// CHALLENGE 6: FIZZBUZZ
// Write a program that prints all the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz", for multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
function fizzBuzz() {}