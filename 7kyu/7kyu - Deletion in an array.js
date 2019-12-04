// 7kyu - Deletion in an array

/* The deleteValues function takes an array and removes elements that answer true to the pred function.
For some reason, some of the elements of the array for which the predicate holds are not deleted...
Can you fix the code?

Bugs | Arrays */

function deleteValues(array, pred) {
    for (var i = 0; i < array.length; i++) {
        if (pred(array[i])) {
            array.splice(i--, 1);
        }
    }
    return array;
}

// function deleteValues(array, pred) {
//     for (var i = array.length - 1; i >= 0; i--) {
//         if (pred(array[i])) {
//             array.splice(i, 1);
//         }
//     }
//     return array;
// }


q = deleteValues([2, 3, 8, 0, 9, 10, 12, 18, 4, 4, 5, 6, 7], (v) => v % 2 == 0)
q