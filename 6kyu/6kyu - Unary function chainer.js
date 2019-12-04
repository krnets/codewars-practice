// 6kyu - Unary function chainer

/* Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)

Should yield the same result as

d(c(b(a(input))))

Fundamentals | Functional Programming | Declarative Programming */

function chained(functions) {
    return function (input) {
        return functions.reduce((a, f) => f(a), input)
    }
}

// const chained = (functions) => [].reduce.bind(functions, (result, fn) => fn(result))
// const chained = require('lodash/flow');

// const id = x => x;
// const uncurry = f => (x,y) => f (x) (y);
// const rcomp = f => g => x => g (f (x));
// const chained = fs => fs.reduce(uncurry(rcomp), id);

// const compose = (f, g) => x => g(f(x))
// const chained = (functions) => (input) => functions.reduce((acc, curr) => compose(acc, curr))(input)
// const chained = ([f, ...fns]) => x => f ? chained(fns)(f(x)) : x


function f1(x){ return x*2 }
function f2(x){ return x+2 }
function f3(x){ return Math.pow(x,2) }

function f4(x){ return x.split("").concat().reverse().join("").split(" ")}
function f5(xs){ return xs.concat().reverse() }
function f6(xs){ return xs.join("_") }

q = chained([f1, f2, f3])(0) // 4 
q
q = chained([f1, f2, f3])(2) // 36 
q
q = chained([f3, f2, f1])(2) // 12 
q
q = chained([f4, f5, f6])("lorem ipsum"), "merol_muspi"
q