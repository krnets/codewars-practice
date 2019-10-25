// const incrementer = nums => nums.map((v, i) => v + (i + 1)).map(v => +String(v).slice(-1))
// const incrementer = nums => nums.map((n, i) => (n + (i + 1)) % 10)
// const incrementer = nums => nums.map((v, i) => +(v + (i + 1) + '').slice(-1))
// const incrementer = a => a.map((x, i) => (x - ~i) % 10)
const incrementer = a => a.map((x, i) => (x - ~i) % 10)


q = incrementer([]) // []
q
q = incrementer([1, 2, 3]) // [2, 4, 6]
q
q = incrementer([4, 6, 7, 1, 3]) // [5, 8, 0, 5, 8]
q
q = incrementer([3, 6, 9, 8, 9]) // [4, 8, 2, 2, 4]
q
q = incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]) // [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2]
q