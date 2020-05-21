// 6kyu - Count characters in your string

/* The main idea is to count all the occuring characters(UTF-8) in string. 
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
What if the string is empty ? Then the result should be empty object literal { } */

// function count(string) {
//     let dict = {};
//     [...string].forEach(v => dict[v] = ++dict[v] || 1)
//     return dict
// }

// const count = require('lodash').countBy;
// import { countBy as count } from 'lodash';

// const count = string => [...string].reduce((dict, v, i, arr) => (dict[v] = (dict[v] ? ++dict[v] : 1), dict), {})
const count = string => [...string].reduce((dict, v) => (dict[v] = dict[v] || 1, dict), {})

q = count("aba") // { a: 2, b: 1 }
q
q = count("") // {}
q