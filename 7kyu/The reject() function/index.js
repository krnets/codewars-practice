// 7kyu - The reject() function

// Let's implement the reject()/Reject() function...
// var odds = reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; }) // => [1, 3, 5]

// function reject(array,iterator) {
//     let a = array.filter(iterator)
//     a
//     return array.filter(v => !a.iterator(v))
// }

// const reject = (array, predicate) => (r = array.filter(predicate), array.filter(v => !r.includes(v)))
const reject = (array, predicate) => array.filter(v => !predicate(v))

q = reject([1, 2, 3, 4, 5, 6], (num) => num % 2 == 0) // [1, 3, 5]);
q