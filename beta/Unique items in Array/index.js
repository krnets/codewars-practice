// Beta - Unique items in Array

/* Javascript libraries Lodash and Underscore provide robust, well tested utilities that can help make 
coding quicker and easier. For this kata: re-implement the _.uniq utility:

Write a function **
uniq
which takes an Array and returns it free of duplicates.**

Once you are done:

    Reuse uniq on future Kata!
    Check out the Lodash/Underscore docs and source code, for
        a version of uniq with many more features
        a huge number of other utilities
    Use Lodash itself on future Kata, with: var _ = require('lodash') (disabled for this Kata) */

// const uniq = require('lodash').uniq

const uniq = arr => [...new Set(arr)]

var list = [1, 2, 1, 3, 1, 4];
q = uniq(list) // [1, 2, 3, 4], 'can find the unique values of an unsorted array'
q

var list = [NaN, 2, NaN, 3, 1, NaN];
q = uniq(list) // [NaN, 2, 3, 1], 'can find the unique values of an unsorted array which includes NaN'
q

var a = {},
    b = {},
    c = {};
q = uniq([a, b, a, b, c]) // [a, b, c], 'works on values that can be tested for equivalency but not ordered'
q