/*
fun top3(s: String): List<String> {
    val re = Regex("([a-z]+'?[a-z']*)", RegexOption.IGNORE_CASE)

    return re.findAll(s)
        .map { it.value.lowercase() }
        .groupingBy { it }
        .eachCount()
        .entries
        .sortedByDescending { it.value }
        .take(3)
        .map { it.key }
}*/

/*
fun top3(s: String): List<String> = "([a-z]+'?[a-z']*)".toRegex(RegexOption.IGNORE_CASE)
    .findAll(s)
    .map { it.value.lowercase() }
    .groupingBy { it }
    .eachCount()
    .entries
    .sortedByDescending { it.value }
    .take(3)
    .map { it.key }
*/

fun top3(s: String): List<String> = "([a-z]+'?[a-z']*)".toRegex()
    .findAll(s.lowercase())
    .map { it.value }
    .groupingBy { it }
    .eachCount()
    .entries
    .sortedByDescending { it.value }
    .take(3)
    .map { it.key }
