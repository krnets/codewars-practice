// 7kyu - Comfortable words

/*  A comfortable word is a word which you can type always alternating the hand you type with 
(assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

That being said, create a function which receives a word and returns true if it's a comfortable word and false otherwise.
The word will always be a string consisting of only ascii letters from a to z.
To avoid problems with image availability, here's the lists of letters for each hand:

    Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
    Right: y, u, i, o, p, h, j, k, l, n, m

Algorithms | Strings | Validation */

function comfortable_word(word) {
    let left = "qwertasdfgzxcvb"
    let right = "yuiophjklnm"
    let arr = [...word].map(v => left.includes(v) ? 1 : right.includes(v) ? -1 : 0)
    for (let i = 1; i < arr.length; i++) {
        let cmp = arr[i] + arr[i - 1]
        if (cmp == 2 || cmp == -2)
            return false
    }
    return true
}

word = 'yams';
q = comfortable_word(word) // true
q

word = 'test';
q = comfortable_word(word) // false
q