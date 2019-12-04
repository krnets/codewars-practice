// 6kyu - Dashatize it

/* Given a number, return a string with dash'-'marks before and after each odd integer, 
but do not begin or end the string with a dash mark.

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

Fundamentals | Strings | Arrays | Regular Expressions | Declarative Programming | Advanced Language Features */

const dashatize = num => Math.abs(num).toString().split(/([13579])/g).filter(Boolean).join('-')
// const dashatize = num => ('' + Math.abs(num)).replace(/\d(?=[13579])|(?:[13579])(?=[02468])/g, '$&-');
// const dashatize = num => isNaN(num) ? 'NaN' : num.toString().match(/([13579]|[02468]+)/g).join('-')
// const dashatize = num => (num && String(num).match(/([13579]|[02468]+)/g).join('-')).toString()
// const dashatize = num => (num + '').replace(/\d/g, d => d & 1 ? `-${d}-` : d).replace(/--/g, '-').replace(/(^-*)|(-*$)/g, '');

q = dashatize(274) // "2-7-4", "Should return 2-7-4"
q
q = dashatize(5311) // "5-3-1-1", "Should return 5-3-1-1"
q
q = dashatize(86320) // "86-3-20", "Should return 86-3-20"
q
q = dashatize(974302) // "9-7-4-3-02", "Should return 9-7-4-3-02"
q
q = dashatize(NaN) // "NaN", "Should return NaN"
q
q = dashatize(0) // "0", "Should return 0"
q
q = dashatize(-1) // "1", "Should return 1"
q
q = dashatize(-28369) // "28-3-6-9", "Should return 28-3-6-9"
q