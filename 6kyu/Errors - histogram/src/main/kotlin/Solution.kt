/*
fun hist(s: String): String = "uwxz"
    .filter { s.contains(it) }
    .map { errorChar ->
        val count = s.filter { errorChar == it }.count()
        val spaces = "".padStart(6 - "$count".length)
        val stars = "*".repeat(count)
        "$errorChar  $count$spaces$stars"
    }
    .joinToString("\r")
*/

fun hist(s: String): String = "uwxz"
    .filter { s.contains(it) }
    .map { errorChar ->
        val count = s.count { errorChar == it }
        val spaces = "".padEnd(6 - "$count".length)
        val stars = "*".repeat(count)
        "$errorChar  $count$spaces$stars"
    }
    .joinToString("\r")

/*
fun hist(s: String): String = s
    .filter { it in "uwxz" }
    .groupingBy { it }
    .eachCount()
    .map { (errorChar, count) ->
        val spaces = "".padEnd(6 - "$count".length)
        val stars = "*".repeat(count)
        "$errorChar  $count$spaces$stars"
    }
    .sorted()
    .joinToString("\r")
*/
