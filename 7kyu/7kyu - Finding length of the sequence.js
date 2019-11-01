// var lengthOfSequence = function (arr, n) {
//     var count = 0;
//     var pos = arr.indexOf(n);

//     while (pos !== -1) {
//       count++;
//       pos = arr.indexOf(n, pos + 1);
//     }
//      if (arr.indexOf(n)== -1) return 0;
//      if (count===1) return 0;
//       if (count>2) return 0;
//       return arr.slice(arr.indexOf(n),arr.lastIndexOf(n)).length+1
//     };

// function lengthOfSequence(arr, el) {
//     let count = 0
//     let position = arr.indexOf(el)

//     while (position !== -1) {
//         count++
//         position = arr.indexOf(el, positions + 1)
//     }

//     if (arr.indexOf(el) == -1 || count == 1 || count > 2) {
//         return 0;
//     }

//     return arr.slice(arr.indexOf(n), arr.lastIndexOf(n)).length + 1;
// }

const lengthOfSequence = (arr, n) =>
    arr.filter(v => v === n).length == 2 ?
    arr.lastIndexOf(n) - arr.indexOf(n) + 1 :
    0


// var lengthOfSequence = function (arr, n) {
//     if (arr.filter(el => el == n).length !== 2)
//         return 0
//     return arr.lastIndexOf(n) - arr.indexOf(n) + 1
// };

q = lengthOfSequence([1, 1], 1) // 2, 'Returns two when there are only two elements in the array');
q
q = lengthOfSequence([1, 2, 3, 1], 1) // 4, 'Returns four for an array of length four and the number to be searched at the boundaries');
q
q = lengthOfSequence([-7, 5, 0, 2, 9, 5], 5) // 5, 'Returns five');
q
q = lengthOfSequence([-7, 6, 2, -7, 4], -7) // 4, 'Returns four');
q
q = lengthOfSequence([],9)
q