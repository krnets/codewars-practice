// 7kyu - String prefix and suffix

const solve = s => s.match(/^(.*).*\1$/)[1].length

q = solve("abcd") // 0
q
q = solve("abcda") // 1
q
q = solve("abcdabc") // 3
q
q = solve("abcabc") // 3
q
q = solve("abcabca") // 1
q
q = solve("aaaa") // 2
q
q = solve("aa") // 1
q
q = solve("a") // 0
q