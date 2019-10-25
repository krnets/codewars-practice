var arr = [1,2] 

// function swapValues() {
//     var args = Array.prototype.slice.call(arguments)
//     args
//     var temp = args[0][0];
//     temp
//     // arr
//     // let a = args[1]
//     // a
//     args[0][0] = args[0][1]

//     args[0][1] = temp;
//     temp
//     // return args[0]
// }
// function swapValues() {
//     return arguments[0].reverse()
// }
// function swapValues() {
//     let args = arguments[0]
//     let temp = args[0]
//     args[0] = args[1]
//     args[1] = temp
// }
function swapValues() {
    var args = Array.prototype.slice.call(arguments)[0];
    var temp = args[0];
    args[0] = args[1];
    args[1] = temp;
}



q = swapValues(arr);
q
q = arr
q
// Test.assertEquals(arr[0], 2, "Failed swapping numbers")
// Test.assertEquals(arr[1], 1, "Failed swapping numbers")
