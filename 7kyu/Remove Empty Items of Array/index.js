// 7kyu - Remove Empty Items of Array

/* In this Kata, you will learn how to remove all empty items in an Array.
In JavaScript, empty items in arrays can be declared by [1, 2,,,3, 4]  (Multiple commas without a value in that index)

The values that are not given a value are empty items, and usually add up with others to form <# empty items>; 
In the example, <2 empty items>

[1, 2, <2 empty items>, 3, 4] should be cleared such that it should be [1, 2, 3, 4]

Before: [1, 2, 3, <5 empty items>, 4, <1 empty item>, null, undefined];
After: [1, 2, 3, 4, null, undefined]; */

// const clean = arr => arr.filter(v => v !== true)

const clean = Object.values

// const clean = arr => arr.filter(_ => 1)
// const clean = arr => arr.filter(_ => true)

q = clean([]) // [], 'Empty Array'
q
q = clean(Array(500000)) // [], '5000000 empty items'
q
q = clean([1, 2]) // [1, 2], 'No empty items here'
q
q = clean([1, 2, , , 3, 4]) // [1, 2, 3, 4], 'Two Empty Items'
q
q = clean([1, 2, [], , 3]) // [1, 2, [], 3], 'Sub-Arrays'
q
q = clean([undefined, null, NaN, false, '', 0]) // [undefined, null, NaN, false, '', 0], 'Falsey Values'
q
q = clean([undefined, , , , null, , NaN, , false, '', 4, 3, 2, 1, 0]) // [undefined, null, NaN, false, '', 4, 3, 2, 1, 0], 'Falsey, Empty, Truthy'
q
