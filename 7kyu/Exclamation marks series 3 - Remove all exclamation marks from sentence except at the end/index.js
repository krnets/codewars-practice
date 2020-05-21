// 7kyu - Exclamation marks series 3 - Remove all exclamation marks from sentence except at the end

function remove(s) {
    let str = ''
    for (let i = s.length - 1; i > 0; i--) {
        if (s[i] == '!') {
            str += s[i]
            continue
        } else {
            var res = s.slice(0, i + 1)
            break
        }
    }
    return res.replace(/\!/g, '') + str
}

// const remove = (s) => s.replace(/!+(?!!*$)/g, '')
// const remove = (s) => s.replace(/!+([^!])/g, '$1')

q = remove("Hi!") // "Hi!"
q
q = remove("Hi!!!") // "Hi!!!"
q
q = remove("!Hi") // "Hi"
q
q = remove("!Hi!") // "Hi!"
q
q = remove("Hi! Hi!") // "Hi Hi!"
q
q = remove("Hi") // "Hi"
q