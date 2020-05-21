// 5kyu - Pipelining and composing functions

/* Let's see 2 ways of applying successive functions to an object:

The purpose of this kata is to think of this kind of code

var result = fn4(fn3(fn2(fn1(obj))));

in terms of pipelining or composition of functions.

1) Pipelining

var result = pipeline(obj
                         , fn1
                         , fn2
                         , fn3
                         , fn4);

for instance:

pipeline([1,2,3,4,5,6] // seed
    , rest // first function to apply
    , rest // second function to apply
    , rest // ..
    , rest
    , first);
=> 5

2) Composition: it should return a function that is the composition of a list of functions, 
where each function consumes the return value of the function that follows.

var compositionFn = compose(fn4, fn3, fn2, fn1);
var result = compositionFn(obj);

for instance

var greet    = function(name){ return "hi: " + name; };
var exclaim  = function(statement){ return statement.toUpperCase() + "!"; };
var welcome = compose(greet, exclaim);
welcome('moe');
=> 'hi: MOE!'

Fundamentals | Functions | Control Flow | Basic Language Features | Composition | Design Principles | Functional Programming | Declarative Programming */

// function pipeline(seed /*, args */ ) {
//     // returns the result of the functions applied to the seed
// };

// function compose() {
//     // returns a function that will be applied to a seed eventually
// };

// function pipeline(seed, ...rest) {
//     return rest.reduce((currVal, currFn) => currFn(currVal), seed)
// }

// function compose(...rest) {
//     return function (seed) {
//         return rest.reduceRight((currVal, currFn) => currFn(currVal), seed)
//     }
// }

const pipeline = (seed, ...fns) => fns.reduce((a, f) => f(a), seed)
// const compose = (...fns) => seed => fns.reduce((a, f) => f(a), seed)  // wrong f(a) order
// const compose = (...fns) => seed => fns.reverse().reduce((a, f) => f(a), seed) // works but not the best practice
const compose = (...fns) => seed => fns.reduceRight((a, f) => f(a), seed)
// const compose = (...fns) => [].reduceRight.bind(fns, (a, f) => f(a))

// const pipeline = (seed, ...fns) => fns.reduce((a, f) => f(a), seed)
// const compose = (...fns) => seed => pipeline(seed, ...fns.reverse())

// const compose = (...fns) => (seed) => fns.reduceRight((a, f) => f(a), seed)
// const pipeline = (seed, ...fns) => compose(...fns.reverse())(seed)

// const callWith = (arg, fn) => fn(arg)
// const pipeline = (init, ...fns) => fns.reduce(callWith, init)
// const compose = (...fns) => init => fns.reduceRight(callWith, init)

q = pipeline() === void 0 // 'It should handle when there is no seed and no function')
q
q = pipeline(42) // 42, 'It should handle when only the seed is specified')
q
q = pipeline(42, (n) => -n) // -42, 'It should handle when a seed and a function are specified')
q

var greet = function (name) {
    return "hi: " + name;
};
var exclaim = function (statement) {
    return statement.toUpperCase() + "!";
};
var welcome = compose(greet, exclaim);
// var welcome = compose(exclaim, greet);

q = welcome('moe') // 'hi: MOE!'
q