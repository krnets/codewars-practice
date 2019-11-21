// 7kyu - Simple Fun #55: Cyclic String

function cyclicString(s) {
    let countLetters = 1
    while (!s.startsWith(s.slice(countLetters)))
        countLetters++
    return countLetters
}

// const cyclicString = (s, n = 1) => s.slice(0, n).repeat(s.length).includes(s) ? n : cyclicString(s, n + 1)
// const cyclicString = (s, i = 1) => s.startsWith(s.slice(i)) ? i : cyclicString(s, i + 1)

q = cyclicString("cabca") // 3
q
q = cyclicString("aba") // 2
q
q = cyclicString("ccccccccccc") // 1
q
q = cyclicString("abaca") // 4
q