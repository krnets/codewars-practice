/*
fun fireFight(s: String): String = s.split(" ").joinToString(" ") { if (it == "Fire") "~~" else it }
*/

/*
fun fireFight(s: String): String = s.replace("Fire", "~~")
*/

fun fireFight(s: String): String {
    val target = "Fire"
    val sb = StringBuilder()
    val aux = StringBuilder()
    var pos = 0

    for (c in s) {
        if (c == target[pos]) {
            aux.append(c)
            pos++

            if (pos == target.length) {
                sb.append("~~")
                pos = 0
                aux.clear()
            }
        } else
            sb.append(c)
    }

    return sb.toString()
}

/*
fun fireFight(s: String): String = s.split("Fire").joinToString("~~")
*/
