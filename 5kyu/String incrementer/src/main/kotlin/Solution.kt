/*
fun incrementString(str: String): String {
    val (word, digits) = str.partition { it.isLetter() }

    val n = if (digits.isEmpty()) "1" else increment(digits.toCharArray())

    return "$word$n"
}

fun increment(digits: CharArray): String {
    var carry = 0

    for (i in digits.indices.reversed()) {
        if (digits[i] == '9') {
            digits[i] = '0'
            carry = 1
        } else {
            digits[i]++
            carry = 0
            break
        }
    }

    val ans = digits.joinToString("")

    return if (carry == 1) "1$ans" else ans
}
*/

/*
fun incrementString(str: String): String {
    val (word, num) = str.partition { it.isLetter() }

    val nextN = if (num.isEmpty()) "1" else (num.toInt() + 1).toString().padStart(num.length, '0')

    return "$word$nextN"
}
*/

/*
fun incrementString(str: String): String {
    val (word, num) = str.partition { it.isLetter() }

    val nextN = ((num.toIntOrNull() ?: 0) + 1).toString().padStart(num.length, '0')

    return "$word$nextN"
}*/

fun incrementString(str: String): String {
    val re = Regex("([0-8]?)(9*)$")

    return str.replace(re) { ((it.value.toIntOrNull() ?: 0) + 1).toString() }
}
