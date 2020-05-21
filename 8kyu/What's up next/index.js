// 8kyu - What's up next?

/* Given a sequence of items and a specific item in that sequence, return the item immediately 
following the item specified. If the item occurs more than once in a sequence, return the item 
after the first occurence. This should work for a sequence of any type.

When the item isn't present or nothing follows it, the function should return  undefined. */

function nextItem(xs, item) {
    let found = false
    for (let i of xs) {
        if (found) return i
        if (i == item) found = true
    }
}

q = nextItem([1, 2, 3, 4, 5, 6, 7], 3) // 4
q
q = nextItem([1, 2, 3, 4, 5, 6, 7, 8], 5) // 6
q
q = nextItem(['a', 'b', 'c'], 'd') // undefined
q
q = nextItem(['a', 'b', 'c'], 'c') // undefined
q
q = nextItem("testing", "t") // "e"
q

function* countFrom(n) {
    for (let i = n;; ++i) yield i;
}
r = countFrom(1)
r
q = nextItem(countFrom(1), 12) // 13
q