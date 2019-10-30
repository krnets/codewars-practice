// 6kyu - Permute a Palindrome

// function permuteAPalindrome(input) {
//     let map = {}
//     let count = 0

//     for (let i = 0; i < input.length; i++) {
//         if (!map[input[i]])
//             map[input[i]] = 1
//         else
//             map[input[i]]++
//     }

//     for (char in map) {
//         if (map[char] % 2 !== 0)
//             count++
//         if (count > 1)
//             return false
//     }

//     return true
// }

function permuteAPalindrome(input) {
    return input
        .split('')
        .sort((a, b) => a.charCodeAt() - b.charCodeAt())
        .join('')
        .replace(/(.)\1/g, '')
        .length <= 1;
}

// q = permuteAPalindrome("a") //  true
// q
// q = permuteAPalindrome("aa") //  true
// q
// q = permuteAPalindrome("baa") //  true
// q
// q = permuteAPalindrome("aab") //  true
// q
// q = permuteAPalindrome("baabcd") // false
// q
// q = permuteAPalindrome("racecars") // false
// q
// q = permuteAPalindrome("abcdefghba") // false
// q
q = permuteAPalindrome("") //  true
q