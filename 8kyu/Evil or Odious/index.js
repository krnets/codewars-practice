// 8kyu - Evil or Odious

/* The number n is Evil if it has an even number of 1's in its binary representation.
The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary representation.
The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, 
function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number. */


// function evil(n) {
//     let count1s = n.toString(2).split('').filter(v => v == '1').length & 1
//     return count1s == 1 ? "It's Odious!" : "It's Evil!"
// }

// const evil = (n) => n.toString(2).match(/1/g).length % 2 ? "It's Odious!" : "It's Evil!"

const evil = (n) => ["It's Evil!", "It's Odious!"][n.toString(2).match(/1/g).length & 1]

// const evil = (n) => `It's ${n.toString(2).match(/1/g).length % 2 ? 'Odious' : 'Evil'}!`

q = evil(1) // "It's Odious!"
q
q = evil(2) // "It's Odious!"
q
q = evil(3) // "It's Evil!"
q