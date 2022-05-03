/*
fun mirror(text: String): String {
    val words = text.split(' ')
    val maxLength = words.maxOf { it.length } + 3
    val stars = "*".repeat(maxLength + 1)
    val mid = words.joinToString("\n") {
        "* ${it.reversed()}".padEnd(maxLength) + "*"
    }
    return "$stars\n$mid\n$stars"
}*/

fun mirror(text: String): String {
    val words = text.split(' ')
    val maxLength = words.maxOf { it.length } + 3
    val stars = "*".repeat(maxLength + 1)

    return words.joinToString("\n", "$stars\n", "\n$stars") {
        "* ${it.reversed()}".padEnd(maxLength) + "*"
    }
}
