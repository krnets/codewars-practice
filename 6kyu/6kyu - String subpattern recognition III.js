// 6kyu - String subpattern recognition III

/* Similar to the previous kata, but this time you need to operate with shuffled strings to identify 
if they are composed repeating a subpattern

Since there is no deterministic way to tell which pattern was really the original one among all the 
possible permutations of a fitting subpattern, return a subpattern with sorted characters, otherwise 
return the base string with sorted characters (you might consider this case as an edge case, 
with the subpattern being repeated only once and thus equalling the original input string).

hasSubpattern("a") === "a"; //no repeated pattern, just one character
hasSubpattern("aaaa") === "a"; //just one character repeated
hasSubpattern("abcd") === "abcd"; //base pattern equals the string itself, no repetitions
hasSubpattern("babababababababa") === "ab"; //remember to return the base string sorted
hasSubpattern("bbabbaaabbaaaabb") === "ab"; //same as above, just shuffled */

function hasSubpattern(string) {
    let gcd = (a, b) => b ? gcd(b, a % b) : a
    let freq = [...string].reduce((count, v) => (count[v] = ++count[v] || 1, count), {})
    let denom = Object.values(freq).reduce(gcd)
    return Object.entries(freq).reduce((res, [v, n]) => [...res, v.repeat(n / denom)], []).sort().join('')
}

q = hasSubpattern("a") // "a"
q
q = hasSubpattern("aaaa") // "a"
q
q = hasSubpattern("abcd") // "abcd"
q
q = hasSubpattern("babababababababa") // "ab"
q
q = hasSubpattern("bbabbaaabbaaaabb") // "ab"
q
q = hasSubpattern("123a123a123a") // "123a"
q
q = hasSubpattern("123A123a123a") // "111222333Aaa"
q
q = hasSubpattern("12aa13a21233") // "123a"
q
q = hasSubpattern("12aa13a21233A") // "111222333Aaaa"
q
q = hasSubpattern("abcdabcaccd") // "aaabbccccdd"
q