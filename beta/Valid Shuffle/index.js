// Beta - Valid Shuffle

/* We are given 3 strings: str1, str2, and str3.

Str3 is said to be a shuffle of str1 and str2 if it can be formed 
by interleaving the characters of str1 and str2 in a way that maintains 
the left to right ordering of the characters from each string.

For example, given str1="abc" and str2="def", str3="dabecf" is a valid shuffle 
since it preserves the character ordering of the two strings.

So, given these 3 strings write a function that detects whether str3 is a valid shuffle of str1 and str2.

Fundamentals | Strings */

const validShuffle = (str1, str2, str3) => {
    return !str3 ? !(str1 || str2) :
        str3[0] == str1[0] && validShuffle(str1.slice(1), str2, str3.slice(1)) ||
        str3[0] == str2[0] && validShuffle(str1, str2.slice(1), str3.slice(1))
}

// const validShuffle = (str1, str2, str3) => str3.length == (str1 + str2).length &&
//     str3.split('').every(v => (str1.indexOf(v) == 0 && !!((str1 = str1.slice(1)) || 1)) || (str2.indexOf(v) == 0 && !!((str2 = str2.slice(1)) || 1)));

q = validShuffle('abc', 'def', 'dabecf') // true
q
q = validShuffle('abc', 'def', 'dabecf') // true
q
q = validShuffle('code', 'wars', 'codewars') // true
q