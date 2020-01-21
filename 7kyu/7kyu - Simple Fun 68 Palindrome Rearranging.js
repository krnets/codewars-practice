// 7kyu - Simple Fun 68 Palindrome Rearranging

/* Given a string s, find out if its characters can be rearranged to form a palindrome.
For s = "aabb", the output should be true.
We can rearrange "aabb" to make "abba", which is a palindrome.
    [input] string s
    A string consisting of lowercase English letters.

    Constraints:
    4 ≤ inputString.length ≤ 50.

    [output] a boolean value
    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise. */

function palindromeRearranging(str) {
    let obj = {};
    [...str].map(v => obj[v] = ++obj[v] || 1)
    return Object.values(obj).filter(v => v & 1).length < 2
}

q = palindromeRearranging("aabb") // true
q
q = palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc") // false
q
q = palindromeRearranging("abbcabb") // true
q
q = palindromeRearranging("zyyzzzzz") // true
q
q = palindromeRearranging("aaabbb") // false
q