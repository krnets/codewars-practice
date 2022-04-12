package countdig

/*
fun nbDig(n: Int, d: Int): Int = (0..n)
    .joinToString { (it * it).toString() }
    .count { it == d.digitToChar() }
*/

fun nbDig(n: Int, d: Int): Int = (0..n).sumOf {
    (it * it).toString()
        .count { it == d.digitToChar() }
}

