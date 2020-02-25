// 6kyu - Insert value into an array

/* Extend the Array object with the function insert(index,value). 
This function must change the original array and insert the value at the given index in the array.

If the index is greater than the array's size, insert the value at the end.

You must return the array to be able to chain the insert function call.
You can use Array's built-in functions to help you.
The 'insert' function must not be enumerable. */

// if (!Array.prototype.insert) {
//     Object.defineProperty(Array.prototype, 'insert', {
//         value: function (index, value) {
//             if (index < 0)
//                 throw "index must be >= 0";
//             if (this == null)
//                 return [value];
//             else if (index >= this.length)
//                 this[this.length] = value;
//             else
//                 this.splice(index, 0, value);
//             return this;
//         }
//     });
// }

if (!Array.prototype.insert) {
    Object.defineProperty(Array.prototype, 'insert', {
        value(index, item) {
            this.splice(index, 0, item)
            return this
        }
    })
}

q = [1, 2, 3].insert(0, 42) // [42,1,2,3]
q
q = [1, 2, 3].insert(0, 0) // [0,1,2,3]]
q
q = ['1', 2, 4].insert(1, 's') // ['1','s',2,4]
q
q = [true, true, true].insert(2, false) // [true,true,false,true]]
q
q = [1, 2, 3].insert(10, 0) // [1,2,3,0]
q
q = [1, 2, 4].insert(3, 1) // [1,2,4,1]
q
q = [0, 0, 0].insert(10, 2) // [0,0,0,2]
q
var arr = [0];
arr.insert(0, 0).insert(10, 2).insert(0, 10)
arr //  [10,0,0,2]