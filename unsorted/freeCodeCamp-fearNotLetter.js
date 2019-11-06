function fearNotLetter(str) {
    let b = str.charCodeAt(0)
    let c = str.charCodeAt(str.length - 1)
    let newString = ''
    let missingLetter = undefined
    
    for (let i = b; i <= c; i++) {
        newString += String.fromCharCode(i)
    }

    for (let i = 0; i < str.length; i++) {
        if (str[i] == newString[i]) {
            continue
        } else {
            i
            missingLetter = newString[i]
            break
        }
    }
    return missingLetter
}

// q = fearNotLetter("abce") === 'd'
// q
// q = fearNotLetter("abcdefghjklmno") === 'i'
// q
// q = fearNotLetter("stvwx") == "u";
// q
// q = fearNotLetter("bcdf") === "e"
// q
q = fearNotLetter("abcdefghijklmnopqrstuvwxyz") === undefined
q