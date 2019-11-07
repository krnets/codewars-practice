// 6kyu - Consecutive Count

function getConsectiveItems(item, key) {
    let s = String(item)
    let count = 0
    let highestSeen = 0
    for (let i = 0; i < s.length; i++) {
        if (s[i] == key) {
            count++
            if (count > highestSeen) {
                highestSeen = count
            }
        } else {
            count = 0
        }
    }
    return highestSeen
}

q = getConsectiveItems(90000, 0) // 4
q
q = getConsectiveItems('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i') // 11
q