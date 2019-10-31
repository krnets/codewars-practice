function palindrome(num) {
    if (!Number.isInteger(num) || num < 0)
        return 'Not valid'

    function isPalindrome(n) {
        n = String(n)
        return [...n].reverse().join('') == n
    }

    num = num < 10 ? 11 : num
    let highNum = num
    let lowNum = num

    if (isPalindrome(num))
        return num
    while (!isPalindrome(highNum))
        highNum++
    while (!isPalindrome(lowNum))
        lowNum--
    return (Math.abs(num - lowNum) === Math.abs(num - highNum) ||
            Math.abs(num - lowNum) > Math.abs(num - highNum)) ? highNum : lowNum
}


q = palindrome(8) // 11
q
q = palindrome(281) // 282
q
q = palindrome(1029) // 1001
q
q = palindrome(1221) // 1221
q
q = palindrome("BGHHGB") // "Not valid"
q
q = palindrome("11029") // "Not valid"
q
q = palindrome(-1029) // "Not valid"
q