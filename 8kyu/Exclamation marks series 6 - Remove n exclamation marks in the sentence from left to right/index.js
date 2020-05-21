// 8kyu - Exclamation marks series 6 - Remove n exclamation marks in the sentence from left to right

// Remove n exclamation marks in the sentence from left to right. n is positive integer.

// function remove(s, n) {
//     while (n--) s = s.replace(/!/, '')
//     return s
// }

// function remove(s, n) {
//     return n > 0 ? remove(s.replace('!', ''), n - 1) : s
// }

function remove(s, n) {
    return s.replace(/!/g, c => (n--) > 0 ? '' : c)
}

q = remove("Hi!", 1) // "Hi"
q
q = remove("Hi!", 100) // "Hi"
q
q = remove("Hi!!!", 1) // "Hi!!"
q
q = remove("Hi!!!", 100) // "Hi"
q
q = remove("!Hi", 1) // "Hi"
q
q = remove("!Hi!", 1) // "Hi!"
q
q = remove("!Hi!", 100) // "Hi"
q
q = remove("!!!Hi !!hi!!! !hi", 1) // "!!Hi !!hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 3) // "Hi !!hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 5) // "Hi hi!!! !hi"
q
q = remove("!!!Hi !!hi!!! !hi", 100) // "Hi hi hi"
q