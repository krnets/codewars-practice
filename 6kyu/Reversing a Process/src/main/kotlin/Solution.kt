package decod

/*
fun decode(r: String): String {
    val (digits, encoded) = r.partition { it.isDigit() }
    val num = digits.toInt()

    return encoded
        .map { c ->
            (0..25)
                .first { i -> c - 'a' == i }
        }
        .flatMap { y ->
            (0..25)
                .filter { x -> x * num % 26 == y }
        }
        .map { i -> 'a' + i }
        .joinToString("")
        .let { plainText ->
            if (plainText.length == encoded.length) plainText
            else "Impossible to decode"
        }
}*/

/*
fun decode(r: String): String = r.partition { it.isDigit() }
    .let { parts ->
        parts.second
            .map { c ->
                (0..25).first { i -> c - 'a' == i }
            }.flatMap { y ->
                (0..25).filter { x -> x * parts.first.toInt() % 26 == y }
            }.map { i -> 'a' + i }
            .joinToString("")
            .let { plainText ->
                if (plainText.length == parts.second.length) plainText
                else "Impossible to decode"
            }
    }
*/

fun decode(r: String): String {
    val (digits, encoded) = r.partition { it.isDigit() }
    val num = digits.toInt() % 26

    for (i in 1..25)
        if (i * num % 26 == 1)
            return encoded.map { 'a' + i * (it - 'a') % 26 }.joinToString("")

    return "Impossible to decode"
}

/*
fun decode(r: String): String {
    return r.takeWhile { it.isDigit() }.toInt().run {
        r.substring("$this".length).map { c ->
            (0..25).filter { n -> n * this % 26 == c - 'a' }
        }.run {
            if (all { it.size == 1 }) map { 'a' + it.first() }.joinToString("")
            else "Impossible to decode"
        }
    }
}
*/
