// function palindrome(num) {

//     function isPalindrome(num) {
//         return (String(+num) === num) ? num === num.split("").reverse().join("") : false;
//     }

//     if (typeof num !== "number" || num < 0) {
//         return "Not valid"
//     }
//     num = String(num);
//     let len = 2,
//         win = [];
//     while (len <= num.length) {
//         for (let i = 0; i + len <= num.length; i++) {
//             let temp = num.substr(i, len)
//             if (+temp !== 0 && isPalindrome(temp) && win.indexOf(+temp) < 0) {
//                 win.push(+temp)
//             }
//         }
//         len++;
//     }
//     return win.length ? win.sort((a, b) => a - b) : "No palindromes found";
// }


function palindrome(num) {
    if (!Number.isInteger(num) || num < 0)
        return 'Not valid'

    let str = String(num)
    let array = []
    let len = 2

    const isPalindrome = n => String(+n) == n ? [...n].reverse().join('') == n : false

    while (len <= str.length) {
        for (let i = 0; i + len <= str.length; i++) {
            let current = str.substr(i, len)
            if (current != 0 && isPalindrome(current) && array.indexOf(+current) < 0)
                array.push(+current)
        }
        len++
    }
    return array.length == 0 ? 'No palindromes found' :
           array.sort((a, b) => a - b)
}

// const isPalindrome = num => String(+num) === num ? num === num.split('').reverse().join('') : false
// let current = str.slice(i, len)
// if (+current !== 0 && isPalindrome(current) && array.indexOf(+current) < 0)
// for (let i = 0; i < str.length; i++)
//     for (let j = i + 1; j <= str.length; j++)
//         if (isPalindrome(str.slice(i, j)))
//             array.push(str.slice(i, j))

// return array.length == 0 ? 'No palindromes found' :
//     array.sort((a, b) => a - b)
//     .map((v, i) => v.length > 1 && v != '0' ? Number(v) : '')
//     .filter((v, i, arr) => arr.indexOf(v) == i)

// function palindrome(num) {
//     return !Number.isInteger(num) || num < 0 ? "Not valid" : /(\d)\d?\1/.test('' + num)
// }

q = palindrome(2) // "No palindromes found"
q
q = palindrome(1551) // [55,1551]
q
q = palindrome(221122) // [11,22,2112,221122]
q
q = palindrome(10015885) // [88,1001,5885]
q
q = palindrome(1002001) // 
q
q = palindrome(13598) // "No palindromes found"
q
q = palindrome("ACCDDCCA") // "Not valid"
q
q = palindrome("1551") // "Not valid"
q
q = palindrome(-4505) // "Not valid"
q



// q = palindrome(2) // 0
// q
// q = palindrome(141221001) // 5
// q
// q = palindrome(1551) // 2
// q
// q = palindrome(13598) // 0
// q
// q = palindrome("ACCDDCCA") // "Not valid"
// q
// q = palindrome("1551") // "Not valid"
// q
// q = palindrome(-4505) // "Not valid"
// q

// q = palindrome(123322367) // true
// q
// q = palindrome(2334) // true
// q
// q = palindrome(1221) // true 
// q
// q = palindrome(2332) // true
// q
// q = palindrome(2) // false
// q
// q = palindrome(1551) // true 
// q 
// q = palindrome(1215) // true 
// q 
// q = palindrome(13598) // false 
// q
// q = palindrome("ACCDDCCA") // "Not valid"
// q
// q = palindrome("1551") // "Not valid"
// q
// q = palindrome(-4505) // "Not valid"
// q