// 6kyu - Simple Fun #396: Find the Longest Substring Consisting of Unique Characters

/* You are given a string s. It's a string consist of letters, numbers or symbols.

Your task is to find the Longest substring consisting of unique characters in s, and return the length of it.

    1 <= s.length <= 10^7
    5 fixed testcases
    100 random testcases, testing for correctness of solution
    100 random testcases, testing for performance of code
    All inputs are valid.
    Pay attention to code performance.
    If my reference solution gives the wrong result in the random tests, please let me know(post an issue).

For s="baacab", the output should be 3.
The non repeating substrings in s are:   "b","c","a","ba","ac","ca","ab","cab"
The longest one is "cab", its length is 3.

For s="abcd", the output should be 4.
The longest one is "abcd", its length is 4.

For s="!@#$%^&^%$#@!", the output should be 7.
The longest substring are "!@#$%^&" and "&^%$#@!", their length both are 7. */

// function longestSubstringOf(s) {
//     let res = []
//     for (let i = 0; i < s.length; i++) {
//         for (let j = i; j <= s.length; j++) {
//             let sub = s.slice(i, j)
//             let set = new Set(sub)
//             if (sub.length == set.size)
//                 res.push(sub)
//         }
//     }
//     return Math.max(...res.map(v => v.length))
// }

// function longestSubstringOf(s) {
//     if (s.length == 0) return 0
//     let result = 1
//     let set = new Set()
//     for (let i = 0, j = 0; j < s.length; j++) {
//         let char = s.charAt(j)
//         if (!set.has(char)) {
//             set.add(char)
//             result = Math.max(result, set.size)
//         } else {
//             while (i < j) {
//                 if (s.charAt(i) == char) {
//                     i++
//                     break
//                 }
//                 set.delete(s.charAt(i))
//                 i++
//             }
//         }
//     }
//     return result;
// }

// function longestSubstringOf(s) {
//     let longest = 0;
//     let unique = '';
//     for (let char of s) {
//         if (!unique.includes(char)) {
//             unique = unique + char;
//             if (unique.length > longest) longest = unique.length;
//         } else {
//             unique = unique.substr(unique.lastIndexOf(char) + 1) + char;
//         }
//     }
//     return longest;
// }

function longestSubstringOf(s) {
    let max = 0;
    let sub = '';
    for (let i = 0; i < s.length; i++) {
        let pos = sub.indexOf(s[i]);
        if (pos !== -1) sub = sub.slice(pos + 1);
        sub += s[i];
        max = Math.max(sub.length, max);
    }
    return max;
}

q = longestSubstringOf("") // 0
q
q = longestSubstringOf("baacab") // 3,"cab is the longest substring."
q
q = longestSubstringOf("abcd") // 4,"abcd is the longest substring."
q
q = longestSubstringOf("hchzvfrkmlnozjk") // 11,"chzvfrkmlno is the longest substring."
q
q = longestSubstringOf("!@#$%^&^%$#@!") // 7,"!@#$%^& is the longest substring."
q
q = longestSubstringOf("abcd".repeat(10000) + "abcde" + "abcd".repeat(10000)) // 5,"abcde is the longest substring. Don't try to write a brute force solution ;-)"
q