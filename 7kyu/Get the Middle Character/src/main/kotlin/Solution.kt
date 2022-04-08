package middle

/*
fun getMiddle(word: String): String {
    var mid = word.length / 2
    return if (word.length % 2 == 0) word.substring(mid - 1, mid + 1) else word[mid].toString()
}*/

/*
fun getMiddle(word: String): String {
    var mid = (word.length - 1) / 2
    return word.drop(mid).dropLast(mid)
}
*/

fun getMiddle(word: String): String {
    var len = word.length
    return word.substring((len - 1) / 2, len / 2 + 1)
}
