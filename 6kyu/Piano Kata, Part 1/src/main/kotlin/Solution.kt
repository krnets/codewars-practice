package pianoKataPartOne

/*
fun blackOrWhiteKey(keyPressCount: Int): String {
    val pattern = "010" + "010100101010".repeat(7) + "0"

    return if (pattern[(keyPressCount - 1) % pattern.length] == '0') "white" else "black"
}
*/

/*
fun blackOrWhiteKey(keyPressCount: Int): String =
    if ("010010100101"[(keyPressCount - 1) % 88 % 12] == '0') "white" else "black"
*/

/*
fun blackOrWhiteKey(keyPressCount: Int): String =
    if (('0' + 1189.toString(2))[(keyPressCount - 1) % 88 % 12] == '0') "white" else "black"
*/

/*
fun blackOrWhiteKey(keyPressCount: Int): String = arrayOf("white", "black")["010010100101".map { it.digitToInt() }[(keyPressCount - 1) % 88 % 12]]
*/

/*
fun blackOrWhiteKey(keyPressCount: Int): String = arrayOf("white", "black")["010010100101".map { it - '0' }[(keyPressCount - 1) % 88 % 12]]
*/

fun blackOrWhiteKey(keyPressCount: Int): String = arrayOf("white", "black")[('0' + 1189.toString(2)).map { it - '0' }[(keyPressCount - 1) % 88 % 12]]
