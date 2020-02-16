// 7kyu - Simple string matching

/* You will be given two strings a and b consisting of lower case letters, 
but a will have at most one asterix character. 

The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) of lowercase letters. 
No other character of string a can be replaced. 

If it is possible to replace the asterix in a to obtain string b, then string b matches the pattern.
If the string matches, return true else false.

solve("code*s","codewars") = true, because we can replace the asterix(*) with "war" to match the second string. 
solve("codewar*s","codewars") = true, because we can replace the asterix(*) with "" to match the second string. 
solve("codewars","codewars") = true, because the strings already match.
solve("a","b") = false

More examples in test cases. */

// const solve = (a, b) => new RegExp(`^${a.replace(/\*/g, "(.)*")}$`).test(b)
const solve = (a, b) => new RegExp(`^${a.replace('*', '.*')}$`).test(b)

q = solve("code*s", "codewars") // true
q
q = solve("codewar*s", "codewars") // true
q
q = solve("code*warrior", "codewars") // false
q
q = solve("c", "c") // true
q
q = solve("*s", "codewars") // true
q
q = solve("*s", "s") // true
q
q = solve("s*", "s") // true
q
q = solve("aa", "aaa") // false
q
q = solve("aa*", "aaa") // true
q
q = solve("aaa", "aa") // false
q
q = solve("aaa*", "aa") // false
q
q = solve("*", "codewars") // true
q