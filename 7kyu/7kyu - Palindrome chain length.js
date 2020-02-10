// 7kyu - Palindrome chain length

/* Number is a palindrome if it is equal to the number with digits in reversed order. 
For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.

Write a method palindrome_chain_length which takes a positive number and returns the number of special steps 
needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". 
If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.

If the input number is already a palindrome, the number of steps is 0.

Input will always be a positive integer.

For example, start with 87:

87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884   */

function palindromeChainLength(n) {
    const isPalindrome = (v) => [...String(v)].reverse().join('') == v
    for (var count = 0, cmp = n; !isPalindrome(cmp); count++)
        cmp = Number(cmp) + Number([...String(cmp)].reverse().join(''))
    return count
}

// function palindromeChainLength(n) {
//     let rev = +[...String(n)].reverse().join('')
//     return n - rev && palindromeChainLength(rev + n) + 1
// }

q = palindromeChainLength(87) // 4
q