const find_average = (array) => array.reduce((a,b) => a + b, 0) / array.length

q = find_average([1,1,1]) // 1
q
q = find_average([1,2,3]) // 2
q