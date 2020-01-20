// 8 kyu - Training JS 17 - Methods of String object--indexOf(), lastIndexOf() and search()

function firstToLast(str, c) {
    return str.search(c) != -1 ? str.lastIndexOf(c) - str.indexOf(c) : -1
}

q = firstToLast("ababc","a") //  2
q
q = firstToLast("ababc","c") //  0
q
q = firstToLast("ababc","d")  // -1
q