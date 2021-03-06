// 6kyu - Remove an Specific Element of an Array

/* You will be given a certain array of length n, such that n > 4, having positive and negative integers 
but there will be no zeroes and all the elements will occur once in it.
We may obtain an amount of n sub-arrays of length n - 1, removing one element at a time (from left to right).
For each subarray, let's calculate the product and sum of its elements with the corresponding absolute value 
of the quotient, q = SubProduct/SubSum (if it is possible, SubSum cannot be 0). Then we select the array with 
the lowest value of |q|(absolute value)

e.g.: we have the array, arr = [1, 23, 2, -8, 5]

Sub Arrays            SubSum    SubProduct         |q|
[23, 2, -8, 5]         22         -1840         83.636363
[1, 2, -8, 5]           0           -80          No value
[1, 23, -8, 5]         21          -920         43.809524
[1, 23, 2, 5]          31           230          7.419355  <--- selected array
[1, 23, 2, -8]         18           368         20.444444

Let's compare the given array with the selected subarray:

[1, 23, 2, -8, 5]
[1, 23, 2,     5]


[` 23 2 -8 5]
[1  ` 2 -8 5]
[1 23 ` -8 5]
[1 23 2  ` 5]
[1 23 2 -8 `]

The difference between them is at the index 3 for the given array, with element -8, 
so we put both things for a result [3, -8].

That means that to obtain the selected subarray we have to take out the value -8 at index 3. 
We need a function that receives an array as an argument and outputs the the pair [index, arr[index]] 
that generates the subarray with the lowest value of |q|.

select_subarray([1, 23, 2, -8, 5]) == [3, -8]

Another case:
select_subarray([1, 3, 23, 4, 2, -8, 5, 18]) == [2, 23]

In Javascript the function will be selectSubarray().
We may have some special arrays that may have more than one solution as the one that follows below.

select_subarray([10, 20, -30, 100, 200]) == [[3, 100], [4, 200]]
If there is more than one result the function should output a 2Darray sorted by the index of the element removed from the array.

Features of the random tests:

Number of tests = 200
length of the array, l, such that 20 <= l <= 100
 */


function selectSubarray(arr) {
    let subArrays = []
    arr.forEach((_, i) => (t = arr.slice(), t.splice(i, 1), subArrays.push(t)))
    let subProduct = v => v.reduce((a, b) => a * b, 1)
    let subSum = v => v.reduce((a, b) => a + b, 0)
    let quotient = v => Math.abs(subProduct(v) / subSum(v))
    let qcalc = subArrays.map(v => quotient(v))
    let smallest = qcalc.reduce((acc, v, i) => (v < acc ? v : acc), Infinity)
    let retrievedArray = subArrays.filter((v, i) => quotient(v) == smallest)[0]
    let val = arr.filter((v, i) => !retrievedArray.includes(v))[0]
    let idx = arr.indexOf(val)
    return [idx, val]
}

// function selectSubarray(arr) {
//     let sum = array => array.reduce((a, b) => a + b, 0);
//     let product = array => array.reduce((a, b) => a * b);
//     let quotient = array => Math.abs(product(array) / sum(array));
//     let res = {};
//     for (let [index, value] of arr.entries()) {
//         let subArray = arr.filter((_, i) => i !== index);
//         res[quotient(subArray)] = [index, value];
//     }
//     return res[Math.min(...Object.keys(res))];
// }
// function selectSubarray(arr) {
//     let sum = arr.reduce((s, n) => s + n, 0)
//     let prod = arr.reduce((p, n) => p * n, 1)
//     let min = [-1, Infinity]
//     for (let i = 0; i < arr.length; i++) {
//         let q = Math.abs((prod / arr[i]) / (sum - arr[i]));
//         if (!isNaN(q) && q < min[1]) min = [i, q];
//     }
//     return [min[0], arr[min[0]]];
// }

// function selectSubarray(arr) {
//     for (var ab, mm, m = Infinity, i = 0; i < arr.length; i++)
//         if ((ab = Math.abs(p = arr.reduce((p, e, j) => p * (j != i ? e : 1), 1) /
//                 arr.reduce((c, e, j) => c + (j != i ? e : 0), 0))) < m) {
//             m = ab;
//             mm = i
//         }
//     return [mm, arr[mm]]
// }

// const selectSubarray = arr => arr.map((x, i) => 
//                                     [Math.abs((t = arr.filter((_, j) => j != i)).reduce((a, b) => a * b, 1) / t.reduce((a, b) => a + b, 0)), i, x])
//                                          .sort((a, b) => a[0] - b[0])[0]
//                                          .slice(1)

// const selectSubarray = arr => (subs = Array.from({ length: arr.length }, 
//     (_, i) => (r = [...arr], r.splice(i, 1), r)), 
//     [arr[i = (g = subs.map(v => Math.abs(v.reduce((a, b) => a * b) / v.reduce((a, b) => a + b, 0))))
//         .indexOf(Math.min(...g))], i].reverse())

q = selectSubarray([1, 23, 2, -8, 5]) // [3, -8]
q
q = selectSubarray([1, 3, 23, 4, 2, -8, 5, 18]) // [2, 23]
q