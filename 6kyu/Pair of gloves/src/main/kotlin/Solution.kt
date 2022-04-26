/*
fun numberOfPairs(gloves: List<String>): Int = gloves
    .groupingBy { it }
    .eachCount()
    .mapValues { it.value / 2 }
    .values.sum()*/

/*
fun numberOfPairs(gloves: List<String>): Int = gloves
    .groupingBy { it }
    .eachCount()
    .values.sumOf { it / 2 }
*/

fun numberOfPairs(gloves: List<String>): Int = gloves
    .groupBy { it }
    .values.sumOf { it.size / 2 }
