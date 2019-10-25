// import * as name from "jest";

function multiplyAll(arr) {
    return function(num) {
        return arr.map(el => el * num)
    }
}

q = multiplyAll([1, 2])(1).length
q
q = multiplyAll([1])(1)
q
q = multiplyAll([1, 2, 3])(1) // [1, 2, 3])
q
q = multiplyAll([1, 2, 3])(2) // [2, 4, 6])
q
q = multiplyAll([1, 2, 3])(0) // [0, 0, 0])
q
q = multiplyAll([])(10) // [], "should return an empty array")
q
