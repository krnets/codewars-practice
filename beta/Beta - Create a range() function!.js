// Beta - Create a range() function!

/* Ragne takes the following parameters and returns an array(range of numbers):

start: starting point.
edge: ending point.
step: incrementing value.

range(0, 500, 50) => [0,50,100,150,200,250,300,350,400,450]

If the start or step is bigger or equals the edge: return empty array.

I will only provide non-negative integers. No need to check for null, undefined etc.

Fundamentals | Arrays | Ranges | Basic Language Features | Numbers | Functions | Control Flow */

// const range = (start, edge, step) => step < edge ? Array.from({length: edge - start}, (_,i) => start + (i * step)).filter(v => v < edge) : []
// const range = (start, edge, step) => step < edge ? Array.from({length: Math.ceil((edge - start) / step)}, (_,i) => start + (i * step)) : []
const range = (start, edge, step) => Array.from({length: Math.round((edge - start) / step)}, (_,i) => start + (i * step))

// const _ = require('lodash');

// function range(start, edge, step) {
//   return step >= edge ? [] : _.range(start, edge, step);
// }

// import { range as _range } from 'lodash';

// function range(start, edge, step) {
//   return step >= edge ? [] : _range(start, edge, step);
// }

q = range(0,10,1) // [0,1,2,3,4,5,6,7,8,9]
q
q = range(1,5,100) // []
q
q = range(0, 500, 50) // [0,50,100,150,200,250,300,350,400,450]
q