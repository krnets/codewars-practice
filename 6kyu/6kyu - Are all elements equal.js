// 6kyu - Are all elements equal?

/* Create (a) method(s) eqAll that determines if all elements of a list are equal.
list can be a String or an Array; return value is a Boolean.
Your method(s) should not be enumerable. Equality should be strict (===).

"aaaaa".eqAll() => true
"abcde".eqAll() => false
[0,0,0].eqAll() => true
[0,1,2].eqAll() => false

"".eqAll() => true
[].eqAll() => true

Bonus points

Bonus points for supporting any (finite) iterable!
This will be tested with Sets and custom Objects.
Note that these may lack a length property, and may not be indexable into. */


// Object.defineProperty(String.prototype, "eqAll", {
//     value: function eqAll() {
//         let prev
//         for (let cur of this) {
//             if (prev === undefined) prev = cur
//             if (cur !== prev) return false
//         }
//         return true
//     }
// })

// Object.defineProperty(Array.prototype, "eqAll", {
//     value: function eqAll() {
//         let prev
//         for (let cur of this) {
//             if (prev === undefined) prev = cur
//             if (cur !== prev) return false
//         }
//         return true
//     }
// })

// function eqAll() {
//     let prev
//     for (let cur of this) {
//         if (prev === undefined) prev = cur
//         if (prev !== cur) return false
//     }
//     return true
// }

// Object.defineProperty(String.prototype, "eqAll", {
//     value: function eqAll() {
//         return new Set(this.split('')).size < 2
//     }
// })

// Object.defineProperty(Array.prototype, "eqAll", {
//     value: function eqAll() {
//         return new Set(this).size < 2
//     }
// })

Object.defineProperty(Object.prototype, "eqAll", {
    value: function eqAll() {
        return [...this].eqAll();
    }
});

Object.defineProperty(Array.prototype, "eqAll", {
    value: function eqAll() {
        return this.every(v => v === this[0]);
    }
});

// Object.defineProperty(String.prototype, "eqAll", { value: function eqAll() { return new Set(this.split('')).size < 2 } })
// Object.defineProperty(Array.prototype,  "eqAll", { value: function eqAll() { return new Set(this).size < 2 } }) 

// Object.defineProperty(String.prototype, "eqAll", { enumerable: false, value: function eqAll() { return new Set(this.split('')).size < 2 } })
// Object.defineProperty(Array.prototype,  "eqAll", { enumerable: false, value: function eqAll() { return new Set(this).size < 2 } }) 

//  String argument
q = "aaaaa".eqAll() // true
q
q = "abcde".eqAll() // false
q
q = "".eqAll() // true
q
// Array argument 
q = [0, 0, 0].eqAll() // true
q
q = [0, 1, 2].eqAll() // false
q
q = [].eqAll() // true
q