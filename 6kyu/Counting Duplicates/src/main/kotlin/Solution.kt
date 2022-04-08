/*
fun duplicateCount(text: String): Int = text
    .groupingBy { it.lowercaseChar() }
    .eachCount()
    .filter { it.value > 1 }
    .size*/

/*
fun duplicateCount(text: String): Int = text
    .groupBy { it.lowercaseChar() }
    .count { it.value.count() > 1 }
*/

fun duplicateCount(text: String): Int = text
    .groupingBy { it.lowercaseChar() }
    .eachCount().values.count { it > 1 }
