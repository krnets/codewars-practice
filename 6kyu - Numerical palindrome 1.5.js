function palindrome(num, s) {
    let listPalindromes = []
    let temp = 0

    if (typeof num != "number" || num < 0 || typeof s != "number")
        return 'Not valid'

    if (String(num).length == 1)
        num = 11

    while (s) {
        temp = num++
        if (temp == [...String(temp)].reverse().join('')) {
            listPalindromes.push(temp)
            s--
        }
    }
    return listPalindromes
}


q = palindrome(6, 4), [11, 22, 33, 44]
q
q = palindrome(75, 1), [77]
q
q = palindrome(19, 3), [22, 33, 44]
q
q = palindrome(101, 2), [101, 111]
q
q = palindrome("ACCDDCCA", 3), "Not valid"
q
q = palindrome(773, "1551"), "Not valid"
q
q = palindrome(-4505, 15), "Not valid"
q

// q = palindrome(1221) // true
// q
// q = palindrome(123322) // false
// q
// q = palindrome("ACCDDCCA") // "Not valid"
// q
// q = palindrome("1221") // "Not valid"
// q
// q = palindrome(-450) // "Not valid"
// q