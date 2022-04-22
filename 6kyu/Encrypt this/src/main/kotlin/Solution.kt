/*
fun encryptThis(text: String): String = text.split(" ")
    .joinToString(" ") {
        val a = it.first().code.toString()
        val b = if (it.length > 1) it.last() else ""
        val c = if (it.length > 3) it.drop(2).take(it.length - 3) else ""
        val d = if (it.length > 2) it.drop(1).take(1) else ""
        a + b + c + d
    }*/

/*
fun encryptThis(text: String): String = text.split(" ")
    .joinToString(" ") {
        it.first().code.toString() +
                it.drop(2).takeLast(1) +
                it.drop(2).dropLast(1) +
                it.drop(1).take(1)
    }
*/

fun encryptThis(text: String): String = text.split(" ")
    .joinToString(" ") {
        it.first().code.toString() +
                it.replace(Regex("^(.)(.)(.*)(.)$"), "$1$4$3$2")
                    .substring(1)
    }
