const sumArray = (arr) => arr == null ? 0 : arr.sort((a,b) => a - b).slice(1,arr.length-1).reduce((accum, cur) => accum + cur, 0)

q = sumArray([ 6, 2, 1, 8, 10 ]) // 16
q
q = sumArray([ 10 ]) // 16
q
a = [10].sort((a,b) => a - b)
a
q = a.slice(1,a.length-1).reduce((accum, cur) => accum + cur, 0)
q
