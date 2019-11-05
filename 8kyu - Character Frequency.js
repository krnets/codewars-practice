// 8kyu - Character Frequency

// const charFreq = message => [...message].reduce((freq, char) => (freq[char] = ++freq[char] || 1, freq), {})

function charFreq(message) {
    let res = {}
    for (let i of message)
        res[i] ? res[i]++ : res[i] = 1
    return res
}

q = charFreq("I like cats")
// {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1});
q