// 7kyu - String reverse slicing 101

// const reverseSlice = str => Array.from({ length: str.length }, (_, i) => [...str.slice(0, i + 1)].reverse().join ``).reverse()
// const reverseSlice = str => Array.from({ length: str.length }, (_, i) => [...str].reverse().join ``.slice(i))
const reverseSlice = str => Array(str.length).fill().map((_, i) => [...str].reverse().join ``.slice(i))


q = reverseSlice('123') // ['321', '21', '1']
q
q = reverseSlice('abcde') // ['edcba', 'dcba', 'cba', 'ba', 'a']
q