function longestRepetition(str) {
    let count = max = 1
    let char
    [...str].map((v, i, a) => {
        if (v == a[i + 1]) {
            count++
            if (count > max)
                [max, char] = [count, v]
        } else
            count = 1
    })
    return (str == '') ? ['', 0] : [char, max]
}

// q = longestRepetition("aaaabb"), ["a", 4]
// q
// q = longestRepetition("bbbaaabaaaa"), ["a", 4]
// q
// q = longestRepetition("cbdeuuu900"), ["u", 3]
// q
// q = longestRepetition("abbbbb"), ["b", 5]
// q
// q = longestRepetition("aabb"), ["a", 2]
// q
q = longestRepetition(""), ["", 0]
q