// 4kyu - Currying vs. Partial Application

function add(a, b, c) {
    return a + b + c
}

var a = 1
var b = 2
var c = 3
var sum = a + b + c

// const curryPartial = (fn) => {
//     return function (a) {
//         return function (b) {
//             return function (c) {
//                 return fn(a, b, c)
//             }
//         }
//     }
// }

const curryPartial = (fn) => {
    return function (a) {
        return function (b) {
            return function (c) {
                return fn(a,b,c)
            }
        }
    }
}


q = add(a, b, c) // sum
q
q = curryPartial(add)(a)(b)(c) // sum
q
q = curryPartial(add, a)(b)(c) // sum
q
q = curryPartial(add, a)(b, c) // sum
q
q = curryPartial(add, a, b, c) // sum
q
q = curryPartial(add, a, b, c, 20) // sum
q
q = curryPartial(add)(a, b, c) // sum
q
q = curryPartial(add)()(a, b, c) // sum
q
q = curryPartial(add)()(a)()()(b, c) // sum
q
q = curryPartial(add)()(a)()()(b, c, 5, 6, 7) // sum
q
q = curryPartial(curryPartial(curryPartial(add, a), b), c) // sum
q
q = curryPartial(curryPartial(add, a, b), c) // sum
q
q = curryPartial(curryPartial(add, a), b, c) // sum
q

q = curryPartial(curryPartial(add, a), b)(c) // sum
q
q = curryPartial(curryPartial(add, a)(b), c) // sum
q

q = curryPartial(curryPartial(curryPartial(add, a)), b, c) // sum
q

// q = Function with two random parameters", function() 
// q

//   function add(a, b) { return a + b; } var a = 1;
//   var b = 2;
//   var sum = a + b;

// q = add(a, b) // sum
// q
q = curryPartial(add)(a)(b) // sum
q
q = curryPartial(add, a, b) // sum
q
q = curryPartial(add, a, b, 20) // sum
q
q = curryPartial(add)(a, b) // sum
q
q = curryPartial(add)()(a, b) // sum
q
q = curryPartial(add)()(a)()()(b) // sum
q
q = curryPartial(add)()(a)()()(b, 5, 6, 7) // sum
q

q = curryPartial(curryPartial(add, a), b) // sum
q

// q = Function with one random parameter", function() 
// q

//   function double(a) {
// return a * 2;
//   }

//   var a = 5;
//   var result = a * 2;

q = double(a), result
q
q = curryPartial(double)(a) // result
q
q = curryPartial(double, a) // result
q
q = curryPartial(double)()(a) // result
q



// q = Function with no parameters", function() 
// q

//   var a = 5;

//   function double() {
//     return a * 2;
//   }

//   var result = a * 2;

q = double() // result
q
q = curryPartial(double) // result
q



// q = Function with four random parameters", function() 
// q

//   function add(a, b, c, d) {
//     return 4*a + 3*b + 2*c + d;
//   }

//   var a = 4;
//   var b = 3;
//   var c = 2;
//   var d = 1;
//   var sum = 4*a + 3*b + 2*c + d;

q = add(a, b, c, d) // sum
q
q = curryPartial(add)(a)(b)(c)(d) // sum
q
q = curryPartial(add)(a, b)(c)(d) // sum
q
q = curryPartial(add, a, b)(c)(d) // sum
q
q = curryPartial(add, a, b)(c, d) // sum
q
q = curryPartial(curryPartial(add, a, b), c, d) // sum
q
q = curryPartial(curryPartial(add, a, b)(c), d) // sum
q
q = curryPartial(curryPartial(add, a)(b, c), d) // sum
q
q = curryPartial(curryPartial(curryPartial(add, a), b), c, d) // sum
q
q = curryPartial(curryPartial(curryPartial(add, a), b), c)(d) // sum
q
q = curryPartial(curryPartial(curryPartial(curryPartial(add, a), b), c), d) // sum
q

// q = State isn't preserved", function() 
// q

//   function add(a, b, c) {
//     return a + b + c;
//   }

//   var add1 = curryPartial(ad //, 1)

q = add1(2, 3) // 6
q
q = add1(4, 5) // 10
q

//   var add2 = curryPartial(add2)(2)
q = add2(3, 4) // 9
q
q = add2(5)(6) // 13
q

//   var add_ = curryPartial //add)
//   var it0 = [add_];
//   var it1 = [].concat(...[0, 1].map(v => it0.map(f => f(v))));
//   var it2 = [].concat(...[0, 2].map(v => it1.map(f => f(v))));
//   var it3 = [].concat(...[0, 4].map(v => it2.map(f => f(v))));
// q = it3, [0, 1, 2, 3, 4, 5, 6, 7],'tree of calls'