// 7kyu - Head, Tail, Init and Last

const head = arr => arr[0]
// const head = arr => +arr.slice(0,1)
const tail = arr => arr.slice(1)
// const init = arr => arr.slice(0,arr.length - 1)
const init = arr => arr.slice(0, -1)
// const last = arr => +arr.slice(-1)
const last = arr => arr[arr.length-1]

// const head = ([head, ...tail]) => head
// const tail = ([head, ...tail]) => tail
// const init = (arr) => arr.slice(0, -1)
// const last = (arr) => arr.slice(-1)[0]


q = head([5,1]) // 5 
q
q = tail([1]) // [] 
q
q = init([1,5,7,9]) // [1,5,7] 
q
q = last([7,2]) // 2 
q