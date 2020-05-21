// 7kyu - Coding Meetup 3 - Higher-Order Functions Series - Is Ruby coming?

/* You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up 
to attend the next coding meetup that you are organising.

Your task is to return:
    true if at least one Ruby developer has signed up; or
    false if there will be no Ruby developers.

For example, given the following input array, your function should return true.

var list1 = [
  { firstName: 'Emma', lastName: 'Z.', country: 'Netherlands', continent: 'Europe', age: 29, language: 'Ruby' },
  { firstName: 'Piotr', lastName: 'B.', country: 'Poland', continent: 'Europe', age: 128, language: 'Javascript' },
  { firstName: 'Jayden', lastName: 'P.', country: 'Jamaica', continent: 'Americas', age: 42, language: 'JavaScript' }
];

The input array will always be valid and formatted as in the example above.

This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas 
which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: 
forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible. */

// const isRubyComing = (list) =>  list.some((_,i) => list[i].language == 'Ruby')
const isRubyComing = (list) => list.some(v => v.language == 'Ruby')


var list1 = [ { firstName: 'Sofia', lastName: 'I.', country: 'Argentina', continent: 'Americas', age: 35, language: 'Java' },
    { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 35, language: 'Python' },
    { firstName: 'Madison', lastName: 'U.', country: 'United States', continent: 'Americas', age: 32, language: 'Ruby' } 
  ];
  
  var list2 = [ { firstName: 'Sofia', lastName: 'I.', country: 'Argentina', continent: 'Americas', age: 35, language: 'Java' },
    { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 35, language: 'Python' } 
  ];
q = isRubyComing(list1) // true
q
q = isRubyComing(list2) // false
q