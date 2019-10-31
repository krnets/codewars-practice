// Remove zeroes without built-in Array filter [incomplete]

// function removeZeros(array) {
// Sort "array" so that all elements with the value of zero are moved to the
// end of the array, while the other elements maintain order.
// [0, 1, 2, 0, 3] --> [1, 2, 3, 0, 0]
// Zero elements also maintain order in which they occurred.
// [0, "0", 1, 2, 3] --> [1, 2, 3, 0, "0"]

// Do not use any temporary arrays or objects. Additionally, you're not able
// to use any Array or Object prototype methods such as .shift(), .push(), etc

// the correctly sorted array should be returned.
// return array;
//   }
// Array.prototype.mf = function (fn) {
//     let newArr = [];
//     for (let i = 0; i < this.length; i++) {
//         if (fn(this[i], i, this)) newArr.push(this[i]);
//     }
//     return newArr;
// }

function removeZeros(array) {

    Array.prototype.mf = function (fn) {
        let newArr = [];
        for (let i = 0; i < this.length; i++) {
            if (fn(this[i], i, this)) newArr.push(this[i]);
        }
        return newArr;
    }

    let zeros = array.mf(v => v === 0)
    let nozero = array.mf(v => v !== 0)

    return [...nozero, ...zeros]
}

// const removeZeros = arr => [...arr.filter(v => v !== 0), ...arr.filter(v => v === 0)]

q = removeZeros([7, 2, 3, 0, 4, 6, 0, 0, 13, 0, 78, 0, 0, 19, 14])
q

// [7, 2, 3, 4, 6, 13, 78, 19, 14, 0, 0, 0, 0, 0, 0];
//   var input = [7, 2, 3, 0, 4, 6, 0, 0, 13, 0, 78, 0, 0, 19, 14],
// solution = [7, 2, 3, 4, 6, 13, 78, 19, 14, 0, 0, 0, 0, 0, 0];

// Test.assertEquals(JSON.stringify(removeZeros(input)), JSON.stringify(solution));