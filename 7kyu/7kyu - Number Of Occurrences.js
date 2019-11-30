// 7kyu - Number Of Occurrences

// Write a functionthat returns the number of occurrences of an element in an array.

// Array.prototype.numberOfOccurrences = function () {
//     return this.filter(v => v == arguments[0]).length
// }

Array.prototype.numberOfOccurrences = function (element) {
    return this.filter(v => v == element).length
}

var arr = [4, 0, 4];
q = arr.numberOfOccurrences(4) // 2
q

var arr = [0, 1, 2, 2, 3];
q = arr.numberOfOccurrences(0) // 1
q
q = arr.numberOfOccurrences(4) // 0
q
q = arr.numberOfOccurrences(2) // 2
q
q = arr.numberOfOccurrences("a") // 0
q