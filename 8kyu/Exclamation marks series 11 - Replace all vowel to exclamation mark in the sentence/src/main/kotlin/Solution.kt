/*
fun replace(s: String): String = s
    .map { if (it in "aeiouAEIOU") '!' else it }
    .joinToString("")*/

/*
fun replace(s: String): String = "[aeiou]".toRegex(RegexOption.IGNORE_CASE).replace(s, "!")
*/

/*
fun replace(s: String): String = Regex("[aeiou]", RegexOption.IGNORE_CASE).replace(s, "!")
*/

fun replace(s: String): String = Regex("(?i)[aeiou]").replace(s, "!")
