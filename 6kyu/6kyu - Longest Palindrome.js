// 6kyu - Longest Palindrome

/* Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
If the length of the input string is 0, the return value must be 0.


"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0 */

function longestPalindrome (s) {
    if (s == [...s].reverse().join('')) return s.length
    let charArray = []
    let countArray = []
    let currentWord = s[0]
    let sLength = s.length + 1
    for (let i = 1, count = 1; i < sLength; i++) {
        if (s[i] === s[i - 1]) {
            count++
            currentWord += s[i]
        } else {
            countArray.push(count)
            charArray.push(currentWord)
            currentWord = s[i]
            count = 1
        }
    }
    let head = 0
    let tail = 0
    let maxWord = ''
    for (let k = 0; k < charArray.length; k++) {
        currentWord = charArray[k]
        tail = head + countArray[k] - 1
        let steps = sLength - countArray[k]
        for (let l = 1; l < steps; l++) {
            if (s[head - l] === s[tail + l]) {
                currentWord = s[head - l] + currentWord + s[tail + l]
            } else {
                maxWord = maxWord.length < currentWord.length ? currentWord : maxWord
                head = tail + 1
                break
            }
        }
    }
    return maxWord.length
}


// q = isPalindrome("zyabyz") 
// q
// q = isPalindrome('racecar')
// q
q = longestPalindrome("racecar")
q
q = longestPalindrome("a") // 1
q
q = longestPalindrome("aa") // 2
q
q = longestPalindrome("baa") // 2
q
q = longestPalindrome("aab") // 2
q
q = longestPalindrome("zyabyz")
q
q = longestPalindrome("baabcd") // 4
q
q = longestPalindrome("baablkj12345432133d") // 9
q