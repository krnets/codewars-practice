package altcaps

/*
fun capitalize(text: String): List<String> {
    var left = StringBuilder()
    var right = StringBuilder()

    text.forEachIndexed { index, c ->
        if (index % 2 == 0) {
            left.append(c.uppercaseChar())
            right.append(c)
        } else {
            left.append(c)
            right.append(c.uppercaseChar())
        }
    }
    return listOf(left.toString(), right.toString())
}
*/

fun capitalize(text: String): List<String> = listOf(StringBuilder(), StringBuilder())
    .also { sb ->
        text.zip(text.uppercase()) { a, b ->
            sb.first().append(if (sb.first().length % 2 == 1) a else b)
            sb.last().append(if (sb.last().length % 2 == 0) a else b)
        }
    }.map { it.toString() }
