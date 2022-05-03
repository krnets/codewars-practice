package binary

/*
private val binCodes = arrayOf("10", "11", "0110", "0111", "001100", "001101", "001110", "001111", "00011000", "00011001")

fun code(str: String): String = str.map { binCodes[it.digitToInt()] }.joinToString("")

fun decode(str: String): String {
    var i = 0
    val bldr = StringBuilder()

    while (i < str.length) {
        var x = 0

        while (str[i + x] == '0') x++

        val sub = str.substring(i, i + 2 * (x + 1))
        bldr.append(binCodes.indexOf(sub))
        i += 2 * (x + 1)
    }
    return bldr.toString()
}*/

fun code(str: String): String =
    str.map { it.digitToInt().toString(2) }
        .joinToString("") {
            "1".padStart(it.length, '0') + it
        }

/*
fun decode(str: String): String {
    val i = str.indexOf('1') + 1

    return if (i == 0) "" else str.substring(i, i + i).toInt(2).toString() + decode(str.substring(i + i))
}
*/

fun decode(str: String): String =
    (str.indexOf('1') + 1)
        .let { i ->
            if (i == 0) ""
            else str.substring(i, i + i).toInt(2).toString() + decode(str.substring(i + i))
        }
