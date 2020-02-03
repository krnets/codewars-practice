// 7kyu - Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer

/* You will be given an array of objects representing data about developers who have signed up to attend the 
next coding meetup that you are organising. The list is ordered according to who signed up first.

Your task is to return one of the following strings:
    < firstName here >, < country here > of the first Python developer who has signed up; or
    There will be no Python developers if no Python developer has signed up.

For example, given the following input array:
var list1 = [
  { firstName: 'Mark', lastName: 'G.', country: 'Scotland', continent: 'Europe', age: 22, language: 'JavaScript' },
  { firstName: 'Victoria', lastName: 'T.', country: 'Puerto Rico', continent: 'Americas', age: 30, language: 'Python' },
  { firstName: 'Emma', lastName: 'B.', country: 'Norway', continent: 'Europe', age: 19, language: 'Clojure' }
];
your function should return Victoria, Puerto Rico.

Notes: The input array will always be valid and formatted as in the example above. */

// function getFirstPython(list) {
//     let result = list.filter(v => v.language == 'Python').map(v => [v.firstName, v.country].join(', '))[0] || []
//     return result.length ? String(result) : 'There will be no Python developers'
// }

function getFirstPython(list) {
    let dev = list.find(x => x.language == 'Python')
    return dev ? dev.firstName + ', ' + dev.country : 'There will be no Python developers'
}

var list1 = [
{ firstName: 'Mark', lastName: 'G.', country: 'Scotland', continent: 'Europe', age: 22, language: 'JavaScript' },
{ firstName: 'Victoria', lastName: 'T.', country: 'Puerto Rico', continent: 'Americas', age: 30, language: 'Python' },
{ firstName: 'Emma', lastName: 'B.', country: 'Norway', continent: 'Europe', age: 19, language: 'Clojure' }
];

var list2 = [
{ firstName: 'Kseniya', lastName: 'T.', country: 'Belarus', continent: 'Europe', age: 29, language: 'JavaScript' },
{ firstName: 'Amar', lastName: 'V.', country: 'Bosnia and Herzegovina', continent: 'Europe', age: 32, language: 'Ruby' },
];

q = getFirstPython(list1) // 'Victoria, Puerto Rico'
q
q = getFirstPython(list2) // 'There will be no Python developers'
q