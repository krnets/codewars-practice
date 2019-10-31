function palindrome(num) {
    if (!Number.isInteger(num) || num < 0)
        return 'Not valid'

    const isPalindrome = n => [...n].reverse().join('') == n && n.length > 1
    str = String(num)

    for (let i = 0; i < str.length; i++)
        for (let j = i + 1; j <= str.length; j++)
            if (isPalindrome(str.slice(i, j)))
                return true
    return false
}

// function palindrome(num) {
//     return !Number.isInteger(num) || num < 0 ? "Not valid" : /(\d)\d?\1/.test('' + num)
// }

q = palindrome(123322367) // true
q
q = palindrome(2334) // true
q
q = palindrome(1221) // true 
q
q = palindrome(2332) // true
q
q = palindrome(2) // false
q
q = palindrome(1551) // true 
q 
q = palindrome(1215) // true 
q 
q = palindrome(13598) // false 
q
q = palindrome("ACCDDCCA") // "Not valid"
q
q = palindrome("1551") // "Not valid"
q
q = palindrome(-4505) // "Not valid"
q