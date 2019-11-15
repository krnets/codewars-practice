// 6kyu - Split Strings

// const solution = str => str.match(/.{2}|.{1}/g).map(v => v.length == 2 ? v : v + '_')
// const solution = str => str.match(/.{1,2}/g).map(v => v.length == 2 ? v : v + '_')
// const solution = str => (str.length % 2 ? str + '_' : str).match(/../g)
// const solution = str => (str + "_").match(/../g)
const solution = str => str.concat('_').match(/../g)

q = solution('abc') // should return ['ab', 'c_']
q
q = solution('abcdef') // should return ['ab', 'cd', 'ef']
q