// const matchArrays = (v, r) => v.map(item => r.indexOf(item) != -1).reduce((a, b) => a + b, 0)
// const matchArrays = (v, r) => v.filter(item => r.indexOf(item) > -1).length
// const matchArrays = (v, r) => v.filter(a => ~r.indexOf(a)).length
// const matchArrays = (v, r) => v.reduce((matched, current) => r.indexOf(current) > -1 ? matched + 1 : matched, 0)
const matchArrays = (v, r) => v.reduce((matched, item) => r.includes(item) ? matched + 1 : matched, 0)

q = matchArrays(['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang']) // 0
q
q = matchArrays(['incapsulation', 'OOP', 'array'], ['time', 'propert', 'paralelism', 'OOP']) // 1
q
q = matchArrays([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) // 4
q