// 6kyu - Are all elements equal? (Infinity version)

/* Create a function eqAll that determines if all elements of a list are equal.
list can be any iterable, and may be infinite. Return value is a Boolean.
Examples

eqAll("aaa") => true
eqAll("abc") => false
eqAll("")    => true

eqAll([0,0,0]) => true
eqAll([0,1,2]) => false
eqAll([])      => true

Notes

For the function result to be true, the iterable must be finite; false, 
however, can result from an element finitely far from the left end. 
There will be no tests with infinite series of equal elements.
Elements will be primitive values; equality should be strict (===). */

// const eqAll = iterable => new Set(iterable).size < 2

function eqAll(iterable) {
    let prev
    for (const cur of iterable) {
        if (prev === undefined) prev = cur
        if (cur !== prev) return false
    }
    return true
}

q = eqAll("aaa") // true
q
q = eqAll("abc") // false
q
q = eqAll("") // true
q
q = eqAll([0, 0, 0]) // true
q
q = eqAll([0, 1, 2]) // false
q
q = eqAll([]) // true
q