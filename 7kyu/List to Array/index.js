// 7kyu - List to Array

/* Linked lists are data structures composed of nested or chained objects, 
each containing a single value and a reference to the next object.

Here's an example of a list:
{value: 1, next: {value: 2, next: {value: 3, next: null}}}

Write a function listToArray that converts a list to an array, like this:
[1, 2, 3]

Assume all inputs are valid lists with at least one value. 
For the purpose of simplicity, all values will be either numbers, strings, or Booleans. */

function listToArray(list) {
    for (var res = [], node = list; node; node = node.next)
        res.push(node.value)
    return res
}

// function listToArray(list) {
//     if (list === null) return []
//     return [list.value, ...listToArray(list.next)]
// }

// const listToArray = (list) => !list ? [] : [list.value].concat(listToArray(list.next))
// const listToArray = (list) => list ? [list.value, ...(listToArray(list.next))] : []

// function* generator(list) {
//     if (list)
//         yield list.value,
//             yield* generator(list.next);
//     else
//         return;
// }

// function listToArray(list) {
//     return Array.from(generator(list));
// }

// Object.prototype[Symbol.iterator] = function*() { yield this.value; if ( this.next ) yield* this.next; } ;
// const listToArray = Array.from;

var list1 = {value: 1, next: {value: 2, next: {value: 3, next: null}}}
var list2 = {value: "foo", next: {value: "bar", next: null}}

q = listToArray(list1), [1, 2, 3]
q
q = listToArray(list2), ["foo", "bar"]
q