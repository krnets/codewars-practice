// 7kyu - No ifs no buts

/* Write a function that accepts two parameters (a and b) and says whether a is smaller than, bigger than, or equal to b.

Here is an example code:

var noIfsNoButs = function (a,b) {
  if(a > b) return a + " is greater than " + b
  else if(a < b) return a + " is smaller than " + b
  else if(a == b) return a + " is equal to " + b
}

There's only one problem...

You can't use if statements, and you can't use shorthands like (a < b) ? true : false
in fact the word "if" and the character "?" are not allowed in the code.

Inputs are guarenteed to be numbers */

// function noIfsNoButs(a, b) {
//     switch (Math.sign(a - b)) {
//         case -1: return a + ' is smaller than ' + b
//         case 0: return a + ' is equal to ' + b
//         case 1: return a + ' is greater than ' + b
//     }
// }

const noIfsNoButs = (a, b) => a < b && `${a} is smaller than ${b}` || a > b && `${a} is greater than ${b}` || `${a} is equal to ${b}`

q = noIfsNoButs(45, 51) // "45 is smaller than 51"
q
q = noIfsNoButs(1, 2) // "1 is smaller than 2"
q
q = noIfsNoButs(-3, 2) // "-3 is smaller than 2"
q
q = noIfsNoButs(1, 1) // "1 is equal to 1"
q
q = noIfsNoButs(100, 100) // "100 is equal to 100"
q
q = noIfsNoButs(100, 80) // "100 is greater than 80"
q
q = noIfsNoButs(20, 19) // "20 is greater than 19"
q