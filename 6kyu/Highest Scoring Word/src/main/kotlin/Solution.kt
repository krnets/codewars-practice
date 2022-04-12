/*
fun high(str: String): String {
    return str.split(" ")
        .map { Pair(it, scoreWord(it)) }
        .maxByOrNull { it.second }!!
        .first
}

fun scoreWord(word: String): Int = word.map { it.code - 'a'.code + 1 }.sum()
*/

fun high(str: String): String = str.split(' ').maxByOrNull { it.sumOf { it - 'a' + 1 } }!!