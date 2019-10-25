const palindrome = num => typeof num != "number" || Math.sign(num) == -1 ? 'Not valid' : [...String(num)].reverse().join('') == num

q = palindrome(1221) // true
q
q = palindrome(123322) // false
q
q = palindrome("ACCDDCCA") // "Not valid"
q
q = palindrome("1221") // "Not valid"
q
q = palindrome(-450) // "Not valid"
q