/*
fun getCount(str: String): Int {
    var vowels = "aeiou"

    return str.filter { vowels.contains(it) }.length
}
*/

fun getCount(str: String): Int = str.count { it in "aeiou" }
