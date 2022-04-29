package updown

/*
fun arrange(strng: String): String {
    val words = strng.split(' ').toMutableList()

    for (i in 0 until words.lastIndex)
        if (words[i + i % 2].length > words[i + 1 - i % 2].length)
            words[i + i % 2] = words[i + 1 - i % 2]
                .also { words[i + 1 - i % 2] = words[i + i % 2] }

    return words.mapIndexed { i, s -> if (i % 2 == 0) s.lowercase() else s.uppercase() }.joinToString(" ")
}
*/

fun arrange(strng: String): String = strng.split(' ').toMutableList().let { words ->

    for (i in 0 until words.lastIndex)
        if (words[i + i % 2].length > words[i + 1 - i % 2].length)
            words[i + i % 2] = words[i + 1 - i % 2]
                .also { words[i + 1 - i % 2] = words[i + i % 2] }

    words.mapIndexed { i, s -> if (i % 2 == 0) s.lowercase() else s.uppercase() }.joinToString(" ")
}
