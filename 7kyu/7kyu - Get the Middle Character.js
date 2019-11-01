// 7kyu - Get the Middle Character

function getMiddle(str) {
    let position
    let length

    if (str.length % 2 == 1) {
        position = str.length / 2
        length = 1
    } else {
        position = str.length / 2 - 1
        length = 2;
    }

    return str.substring(position, position + length)
}


q = getMiddle("test") // "es"
q
q = getMiddle("testing") // "t"
q
q = getMiddle("middle") // "dd"
q
q = getMiddle("A") //"A"
q