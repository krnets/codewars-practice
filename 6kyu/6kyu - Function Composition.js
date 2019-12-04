// 6kyu - Function Composition

/* Function composition is a mathematical operation that mainly presents itself in lambda calculus and computability. 
It is explained well here, but this is my explanation, in simple mathematical notation:

f3 = compose( f1 f2 )
   Is equivalent to...
f3(a) = f1( f2( a ) )

Your task is to create a compose function to carry out this task, which will be passed two functions or lambdas. 
Remember that the resulting composed function may be passed multiple arguments!

compose(f, g)(x) => f( g( x ) )

Fundamentals | Functional Programming | Declarative Programming | Higher-order Functions | 
Functions | Control Flow | Basic Language Features | Lambdas | Composition | Design Principles */

// function compose(f, g) {
//     return function () {
//         return f(g.apply(this, arguments));
//     };
// }

// function compose(f, g) {
//     return function (...a) {
//         return f(g(...a));
//     }
// }

// const compose = (f, g) => (...x) => f(g(...x))
// const {compose} = require('lodash');
// ({compose}=require('ramda'))

const add1 = (a) => a + 1
const id = (a) => a

q = compose(add1, id)(0) // 1
q