// 6kyu - Mirror, Mirror

/* Write a function evilTwin(obj) which returns a new object with all the same properties as obj, 
and with an additional property hasGoatee set to true.

For example:

var orig = {x: 5};
console.log(orig.x) // -> 5
console.log(orig.hasGoatee) // -> undefined
var twin = evilTwin(orig);
console.log(twin.x) // -> 5
console.log(twin.hasGoatee) // -> true

If the original object is modified, its twin should reflect the changes so:

orig.z = 12
console.log(twin.z) // -> 12  */

// function evilTwin(obj) {
//     let twin = Object.create(obj)
//     twin.hasGoatee = true
//     return twin
// }

// const evilTwin = obj => Object.create(obj, {
//     hasGoatee: {
//         value: true
//     }
// })

const evilTwin = obj => Object.create(obj, { hasGoatee: { value: true } })


var obj = {
    x: 5
};
var twin = evilTwin(obj);
twin

q = twin.hasGoatee // true
q
q = obj.hasGoatee == null // true
q
obj
twin
q = twin.x
q
