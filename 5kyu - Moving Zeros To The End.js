// 5kyu - Moving Zeros To The End

const moveZeros = arr => [...arr.filter(v => v !== 0), ...arr.filter(v => v === 0)]

q = moveZeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
q
q = JSON.stringify(moveZeros([1,2,0,1,0,1,0,3,0,1]))
q
q = JSON.stringify([ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
q