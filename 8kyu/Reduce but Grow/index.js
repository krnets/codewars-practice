// const grow = x => x.reduce((a,b) => a * b)
const grow = x => eval(x.join('*'))


q = grow([1, 2, 3]) // 6);
q
q = grow([4, 1, 1, 1, 4]) // 16); 
q
q = grow([2, 2, 2, 2, 2, 2]) // 64); 
q