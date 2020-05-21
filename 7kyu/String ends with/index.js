// const solution = (str, ending) => ending.length == 0 ? true : (str.slice(-ending.length) == ending)
 
const solution = (str, ending) => str.endsWith(ending)

// q = solution('abcde', 'cde') //, true)
// q
// q = solution('abcde', 'abc') //, false)
// q
// q = solution('abc', '') //, false)
// q