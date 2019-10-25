// const invert = arr => arr.map(v => v < 0 ? Math.abs(v) : -v)

// const invert = arr => arr.map(v => v == 0 ? v : -v)

// const invert = arr => arr.map(num => -num)

const invert = arr => arr.map(num => 0 - num)

q = invert([1,2,3,4,5]) // [-1,-2,-3,-4,-5]);
q
q = invert([1,-2,3,-4,5]) // [-1,2,-3,4,-5]);
q
q = invert([]) // []);
q
q = invert([0]) // [0]);
q