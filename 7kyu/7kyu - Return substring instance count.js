// 7kyu - Return substring instance count

const solution = (fullText, searchText) => (fullText.match(RegExp(searchText, 'g')) || []).length
// const solution = (fullText, searchText) => fullText.split(searchText).length - 1
// const solution = (f, s) => (idx = f.indexOf(s)) == -1 ? 0 : 1 + solution(f.slice(idx + 1), s)

q = solution('abcdeb', 'b') // 2
q
q = solution('abc', 'b') // 1
q
q = solution('abbc', 'bb') // 1
q