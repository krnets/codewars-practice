/*
fun reverseLetter(str: String): String {
    return str.replace("[^a-z]".toRegex(), "").reversed()
}*/

fun reverseLetter(str: String): String {
    return str.filter { it.isLetter() }.reversed()
}
