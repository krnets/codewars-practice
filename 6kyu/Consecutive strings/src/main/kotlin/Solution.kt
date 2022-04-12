package longestconsec

fun longestConsec(strarr: Array<String>, k: Int): String {
    if (k <= 0 || k > strarr.size) return ""

    return strarr.asSequence()
        .windowed(k)
        .map { it.joinToString("") }
        .maxByOrNull { it.length } ?: ""
}

/*
package longestconsec

fun longestConsec(strarr: Array<String>, k: Int): String =
    k.takeIf { it > 0 }?.let {
    strarr.asSequence()
        .windowed(k, 1)
        .map { it.joinToString("") }
        .maxByOrNull { it.length } ?: ""
    } ?: ""
*/
