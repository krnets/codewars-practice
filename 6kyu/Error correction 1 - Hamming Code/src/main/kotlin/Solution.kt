package algos

/*
fun encode(text: String): String {
    return text.map { c ->
        c.code.toString(2)
            .padStart(8, '0')
            .map { "$it".repeat(3) }
            .joinToString("")
    }.joinToString("")
}
*/

/*
fun decode(bits: String): String {
    return bits.chunked(24)
        .map { triple ->
            triple.chunked(3).map { bit ->
                if (bit.count { it == '1' } > 1) 1 else 0
            }.joinToString("")
        }
        .map { Integer.parseInt(it, 2) }
        .map { it.toChar() }
        .joinToString("")
}*/

/*
fun encode(text: String): String = text.map { c ->
    c.code.toString(2)
        .padStart(8, '0')
        .map { "$it".repeat(3) }
        .joinToString("")
    }.joinToString("")

*/

/*
fun decode(bits: String): String = bits.chunked(3)
    .map { bit -> if (bit.count { it == '1' } > 1) 1 else 0 }
    .joinToString("")
    .chunked(8)
    .map { Integer.parseInt(it, 2).toChar() }
    .joinToString("")
*/

fun encode(text: String): String = text.flatMap { c ->
    c.code.toString(2)
        .padStart(8, '0')
        .map { "$it".repeat(3) }
    }.joinToString("")

fun decode(bits: String): String = bits.chunked(3)
    .map { bit -> if (bit.count { it == '1' } > 1) '1' else '0' }
    .chunked(8)
    .map { Integer.parseInt(it.joinToString(""), 2).toChar() }
    .joinToString("")
