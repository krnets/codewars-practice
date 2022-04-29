package solution

/*
fun stringExpansion(s: String): String {
    val sb = StringBuilder()
    var i = 0

    while (i < s.length) {
        if (s[i].isDigit()) {
            var j = i + 1
            val r = s[i].digitToInt()

            while (j < s.length && s[j].isLetter()) {
                j++
            }
            i++
            while (i < j) {
                sb.append("${s[i]}".repeat(r))
                i++
            }
        } else {
            sb.append(s[i])
            i++
        }
    }
    return sb.toString()
}
*/

/*
fun stringExpansion(s: String): String {
    var r = 1
    return buildString {
        s.forEach {
            if (it.isDigit())
                r = it.digitToInt()
            else append("$it".repeat(r))
        }
    }
}
*/

/*
fun stringExpansion(s: String): String {
    var r = 1

    return s.fold(StringBuilder()) { sb: StringBuilder, c: Char ->
        when {
            c.isDigit() -> r = c.digitToInt()
            else -> sb.append("$c".repeat(r))
        }
        sb
    }.toString()
}
*/

/*
fun stringExpansion(s: String): String {
    return Regex("(?i)\\d?[a-z]+").findAll(s)
        .joinToString("") { m ->
            if (m.value.first().isDigit()) {
                val r = m.value.first().digitToInt()
                m.value.substring(1).map { "$it".repeat(r) }.joinToString("")
            } else m.value
        }
}
*/

fun stringExpansion(s: String): String {
    var times = 1
    val sb = StringBuilder()

    s.forEach {
        if (it.isDigit()) times = it.digitToInt()
        else sb.append("$it".repeat(times))
    }
    return sb.toString()
}
