// Beta - A function within a function

// Given an input n, write a function always that returns a function which returns n. 

function always(n) {
    return function () {
        return n
    }
}

// const always = n => () => n


q = always(true)() // 'A function that is always true will return true')
q
let three = always(3)
q = three() // returns 3
q