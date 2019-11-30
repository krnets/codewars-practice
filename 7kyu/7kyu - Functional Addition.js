// 7kyu - Functional Addition

/* Create a function add(n)/Add(n) which returns a function that always adds n to any number

var addOne = add(1);
addOne(3); // 4

var addThree = add(3);
addThree(3); // 6

Fundamentals | Functional Programming | Declarative Programming */

function add(n) {
    return function (m) {
        return n + m
    }
}

// const add = n => m => n + m

q = add(1)(3) // 4, 'add one to three equals four'
q