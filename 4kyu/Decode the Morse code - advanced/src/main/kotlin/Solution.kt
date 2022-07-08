/*
fun decodeBits(bits: String): String {
    var bits = bits.trim('0')
    var rate = 1
    var curr = rate

    if (bits.toSet().size > 1) {
        while (curr < 5) {
            curr++

            if (bits.chunked(curr).all { it.length == curr && it.toSet().size == 1 })
                rate = curr
        }
    } else rate = bits.length

    return bits.split("0".repeat(7 * rate)).joinToString(" ".repeat(7)) { word ->

        word.split("000".repeat(rate))

            .joinToString(" ") { letter ->

                letter.chunked(rate)
                    .map {
                        if (it.first() == '1') '1'
                        else '0'

                    }.joinToString("")
                    .split("0")
                    .map { if (it.length == 3) '-' else '.' }
                    .joinToString("")
            }
    }
}

fun decodeMorse(code: String): String = code.split(" ".repeat(7))
    .joinToString(" ") { word ->
        word.split(" ")
            .joinToString("") { MORSE_CODE[it] ?: "" }
    }
*/

val MORSE_CODE = mutableMapOf(
    ".-" to "A",
    "-..." to "B",
    "-.-." to "C",
    "-.." to "D",
    "." to "E",
    "..-." to "F",
    "--." to "G",
    "...." to "H",
    ".." to "I",
    ".---" to "J",
    "-.-" to "K",
    ".-.." to "L",
    "--" to "M",
    "-." to "N",
    "---" to "O",
    ".--." to "P",
    "--.-" to "Q",
    ".-." to "R",
    "..." to "S",
    "-" to "T",
    "..-" to "U",
    "...-" to "V",
    ".--" to "W",
    "-..-" to "X",
    "-.--" to "Y",
    "--.." to "Z",  //------------------------
    "-----" to "0",
    ".----" to "1",
    "..---" to "2",
    "...--" to "3",
    "....-" to "4",
    "....." to "5",
    "-...." to "6",
    "--..." to "7",
    "---.." to "8",
    "----." to "9",  //------------------------
    ".-.-.-" to ".",
    "--..--" to ",",
    "..--.." to "?",
    ".----." to "'",
    "-.-.--" to "!",
    "-..-." to "/",
    "-.--." to "(",
    "-.--.-" to ")",
    ".-..." to "&",
    "---..." to "=>",
    "-.-.-." to ";",
    "-...-" to "=",
    ".-.-." to "+",
    "-....-" to "-",
    "..--.-" to "_",
    ".-..-." to "\"",
    "...-..-" to "$",
    ".--.-." to "@",
    "...---..." to "SOS"
)


/*
fun decodeBits(bits: String): String {
    var bits = bits.trim('0')
    val rate = "0+|1+".toRegex().findAll(bits).map { it.value.length }.min()

    return bits.replace("111".repeat(rate), "-")
        .replace("000".repeat(rate), " ")
        .replace("1".repeat(rate), ".")
        .replace("0".repeat(rate), "")
}

fun decodeMorse(code: String): String =
    code.split("  ").joinToString(" ") { word ->
        word.split(" ").joinToString("") { MORSE_CODE[it] ?: " " }
    }

*/

/*
fun decodeBits(bits: String): String = bits.trim('0')
    .let { it to ("0+|1+".toRegex().findAll(it).map { m -> m.value.length }.min() ?: 1) }
    .run {
        first.replace("0".repeat(second), "0")
            .replace("1".repeat(second), "1")
    }
    .replace("0".repeat(7), "  ")
    .replace("0".repeat(3), " ")
    .replace("111", "-")
    .replace("1", ".")
    .replace("0", "")

fun decodeMorse(code: String): String =
    code.split("  ").joinToString(" ") { word ->
        word.split(" ").joinToString("") { MORSE_CODE[it]!! }
    }
*/

fun decodeBits(bits: String): String = bits.trim('0')
    .let { it to ("0+|1+".toRegex().findAll(it).map { m -> m.value.length }.min() ?: 1) }
    .run {
        first.replace("111".repeat(second), "-")
            .replace("000".repeat(second), " ")
            .replace("1".repeat(second), ".")
            .replace("0".repeat(second), "")
    }

fun decodeMorse(code: String): String = code.split(" ").joinToString("") { MORSE_CODE[it] ?: " " }
