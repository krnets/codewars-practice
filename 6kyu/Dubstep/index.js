// 6kyu - Dubstep

const songDecoder = song => song.replace(/(WUB)+/g, ' ').trim()

q = songDecoder("AWUBBWUBC") // "A B C" // "WUB should be replaced by 1 space")
q
q = songDecoder("AWUBWUBWUBBWUBWUBWUBC") // "A B C" // "multiples WUB should be replaced by only 1 space")
q
q = songDecoder("WUBAWUBBWUBCWUB") // "A B C" // "heading or trailing spaces should be removed")
q
