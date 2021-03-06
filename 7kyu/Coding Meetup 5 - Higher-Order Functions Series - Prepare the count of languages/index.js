// 7kyu - Coding Meetup 5 - Higher-Order Functions Series - Prepare the count of languages

/* You will be given an array of objects representing data about developers who have signed up to attend 
the next coding meetup that you are organising.

Your task is to return an object (associative array in PHP) which includes the count of each 
coding language represented at the meetup.

For example, given the following input array:

var list1 = [
  { firstName: 'Noah', lastName: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'C' },
  { firstName: 'Anna', lastName: 'R.', country: 'Liechtenstein', continent: 'Europe', age: 52, language: 'JavaScript' },
  { firstName: 'Ramon', lastName: 'R.', country: 'Paraguay', continent: 'Americas', age: 29, language: 'Ruby' },
  { firstName: 'George', lastName: 'B.', country: 'England', continent: 'Europe', age: 81, language: 'C' },
];

your function should return the following object (associative array in PHP):

{ C: 2, JavaScript: 1, Ruby: 1 }

    The order of the languages in the object does not matter.
    The count value should be a valid number.
    The input array will always be valid and formatted as in the example above.


This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which 
have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: 
forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible. */

var list1 = [
    { firstName: 'Noah', lastName: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'C' },
    { firstName: 'Anna', lastName: 'R.', country: 'Liechtenstein', continent: 'Europe', age: 52, language: 'JavaScript' },
    { firstName: 'Ramon', lastName: 'R.', country: 'Paraguay', continent: 'Americas', age: 29, language: 'Ruby' },
    { firstName: 'George', lastName: 'B.', country: 'England', continent: 'Europe', age: 81, language: 'C' },
  ];

// function countLanguages(list) {
//     let count = {}
//     list.forEach(v => count[v.language] = ++count[v.language] || 1)
//     return count
// }

// function countLanguages(list) {
//     let count = {}
//     list.forEach(({language:v}) => count[v] = ++count[v] || 1)
//     // list.forEach(({language:v}) => count[v] ? count[v]++ : count[v] = 1)
//     return count
// }

// function countLanguages(list) {
//     return list.reduce((count, v) => {
//         if (v.language in count) ++count[v.language]
//         else count[v.language] = 1;
//         return count
//     }, {})
// }

// function countLanguages(list) {
//     return list.reduce((count, v) => {
//         // (v.language in count ? ++count[v.language] :  count[v.language] = 1);
//         count[v.language] = ++count[v.language] || 1; return count
//     }, {})
// }

const countLanguages = (list) => list.reduce((count, v) => { count[v.language] = ++count[v.language] || 1; return count }, {})

q = countLanguages(list1) //  { C: 2, JavaScript: 1, Ruby: 1 };
q