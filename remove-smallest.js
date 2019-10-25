function removeSmallest(numbers) {
    let low = {
        num: Infinity,
        idx: 0
    }

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] < low['num']) {
            low['num'] = numbers[i]
            low['idx'] = i
        }
    }

    return numbers.slice(0, low['idx']).concat(numbers.slice(low['idx'] + 1))

}


q = removeSmallest([11, 12, 30, 14, 52])
q

function removeSmallest_2(numbers) {
    let indexOfMin = numbers.indexOf(Math.min(...numbers));
    return [...numbers.slice(0, indexOfMin), 
            ...numbers.slice(indexOfMin + 1)];
  }


q = removeSmallest_2([11, 2, 3, 41, 52])
q

const removeSmallest_3 = numbers => numbers
        .filter((n,i) => i !== numbers.indexOf(Math.min(...numbers)));

q = removeSmallest_3([113, 21, 36, 41, 59])
q

nb = [113, 21, 36, 41, 59]
q = Math.max(...nb)
q


/* -------------------------------------------*/
// Test.describe("removeSmallest", function() {
//     Test.it("works for the examples", function() {
//       Test.assertSimilar(removeSmallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]");
//       Test.assertSimilar(removeSmallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]");
//       Test.assertSimilar(removeSmallest([2, 2, 1, 2, 1]), [2, 2, 2, 1], "Wrong result for [2, 2, 1, 2, 1]");
//       Test.assertSimilar(removeSmallest([]), [], "Wrong result for []");
//     });
//     Test.it("returns [] if the list has only one element", function() {
//       for (let i = 0; i < 10; ++i) {
//         let x = ~~(Math.random() * 400);
//         Test.assertSimilar(removeSmallest([x]), [], `Wrong result for ${[x]}`);

//     });
//     function randomArray(length) {
//       return Array.from({length: length}, () => ~~(Math.random() * 400));
//     }

//     Test.it("returns a list that misses only one element", function() {
//       for(let i = 0; i < 10; ++i) {
//         let arr = randomArray(~~(Math.random() * 10) + 1);
//         let l = arr.length;
//         Test.assertSimilar(removeSmallest(arr).length, l - 1, `Wrong result for ${arr}`);
//       }
//     });
//   });