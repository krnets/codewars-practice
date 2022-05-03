/*
fun numberAndIPaddress(s: String): String =
    if (s.contains('.')) {
        s.split('.')
            .joinToString("") { it.toInt().toString(2).padStart(8, '0') }
            .toLong(2).toString()
    } else {
        s.toLong().toString(2).padStart(32, '0')
            .chunked(8)
            .map { it.toInt(2) }
            .joinToString(".")
    }
*/

/*
fun numberAndIPaddress(s: String): String = when {
    s.contains('.') ->
        s.split('.')
            .joinToString("") { it.toInt().toString(2).padStart(8, '0') }
            .toLong(2).toString()
    else ->
        s.toLong().toString(2).padStart(32, '0')
            .chunked(8)
            .map { it.toInt(2) }
            .joinToString(".")
}
*/

fun numberAndIPaddress(s: String): String = when {
    ('.' in s) -> s.split('.')
        .fold(0L) { acc, octet -> acc * 256 + octet.toLong() }
        .toString()
    else -> (3.downTo(0))
        .map { s.toLong() shr 8 * it and 255 }
        .joinToString(".")
}
