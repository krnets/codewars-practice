/*
fun alphaSeq(str: String): String {
    val letters = str.lowercase().asIterable().sorted().toList()
    var list = mutableListOf<String>()

    letters.forEach {
        var s = it.uppercase() + it.toString().repeat(it - 'a')
        list.add(s)
    }
    return list.joinToString(",")
}*/

fun alphaSeq(str: String): String = str.lowercase()
    .asIterable()
    .sorted()
    .joinToString(",") { it.uppercase() + "$it".repeat(it - 'a') }
