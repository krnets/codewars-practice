const arr2bin = (arr) =>  {
    let a = arr.filter(Number.isInteger).reduce((a,b) => a + b, 0).toString(2)

    // filter(Number).reduce((a,b) => a + b, 0).toString(2)
    a
    // return arr.filter(isNaN) ? 'NaN' : a
    // return arr[0] == null && arr.length > 1 ? 'NaN' : a
    return arr.filter((val, index) => arr[index] == null) ? 0 : 1

}
// arr.reduce((a, b) => a + b, 0).toString(2)

q = arr2bin([1, 2]) // "11"
q
q = arr2bin([1, 2, 3, 4, 5]) // "1111"
q
q = arr2bin([1, 10, 100, 1000]), "10001010111"
q
q = arr2bin([null]) // "0"
q
q = arr2bin([true, true, false, 15]) // "1111"
q
q = arr2bin([null,2,42,4,4]) // [ NaN, 2, 42, 4, 4 ]
q