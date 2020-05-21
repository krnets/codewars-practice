// 7kyu - Unpacking Arguments

/* Create a function, spread, that takes a function and a list of arguments to be applied to that function. 
This function returns the result of calling the given function/lambda with the given arguments.

spread(someFunction, [1, true, "Foo", "bar"] ) 
// is the same as...
someFunction(1, true, "Foo", "bar")

Fundamentals | Arguments | Basic Language Features | Declarative Programming | 
Functions | Control Flow | Lambdas | Functional Programming | Higher-order Functions */


// function spread(func, args) {
//     return func(...args)
// }

function spread(func, args) {
    return func.apply(this, args)
}

q = spread(function (x, y) { return x + y }, [1, 2]) // 3 
// Equivalent: (function(x,y){return x+y})(1,2)
q