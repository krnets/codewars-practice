fun wave(str: String): List<String> {
    var list = mutableListOf<String>()

    str.forEachIndexed { i, c ->
        if (c != ' ') {
            list.add(
                str.substring(0, i) + str[i].uppercaseChar() + str.substring(i + 1)
            )
        }
    }
    return list
}

/*
fun wave(str: String): List<String> {
    var list = mutableListOf<String>()

    str.forEachIndexed { i, c ->
        if (c != ' ') {
            var chars = str.toCharArray()
            chars[i] = chars[i].uppercaseChar()
            list.add(String(chars))
        }
    }
    return list
}
*/

/*
fun wave(str: String): List<String> = str.indices
    .map { str.take(it) + str.drop(it).capitalize() }
    .filter { it != str }
*/
