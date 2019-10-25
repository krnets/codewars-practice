function negationValue(string, value) {
    for (let i in string)
        value = !value
    return value
}

q = negationValue("!", false) // true, "Wrong!"
q
q = negationValue("!", true) // false, "Wrong!"
q
q = negationValue("!!!", []) // false, "Wrong!"
q