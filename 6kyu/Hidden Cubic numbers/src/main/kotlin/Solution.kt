package solution

/*
object Cubes {
    fun isSumOfCubes(s: String): String {
        var nums = Regex("\\d{1,3}").findAll(s)
            .map { it.value }
            .filter { num ->
                num.map { it.digitToInt() }
                    .sumOf { it * it * it } == num.toInt()
            }

        return if (nums.count() == 0) "Unlucky"
        else "${nums.joinToString(" ")} ${nums.sumOf { it.toInt() }} Lucky"
    }
}*/

/*
object Cubes {
    fun isSumOfCubes(s: String): String = Regex("\\d{1,3}").findAll(s)
        .map { it.value.toInt() }
        .filter { num ->
            num.toString().map { it.digitToInt() }
                .sumOf { it * it * it } == num
        }.let { nums ->
            if (nums.count() == 0) "Unlucky"
            else "${nums.joinToString(" ")} ${nums.sum()} Lucky"
        }
}
*/

/*
object Cubes {
    fun isSumOfCubes(s: String): String =
        Regex("\\d{1,3}").findAll(s)
            .map { it.value.toInt() }
            .filter { num ->
                num.toString().map { it.digitToInt() }
                    .sumOf { it * it * it } == num
            }.let { nums ->
                if (nums.none()) "Unlucky"
                else "${nums.joinToString(" ")} ${nums.sum()} Lucky"
            }
}
*/

/*
object Cubes {
    fun isSumOfCubes(s: String): String = Regex("\\d{1,3}").findAll(s)
        .map { Pair(it.value, it.value.toInt()) }
        .filter { pair ->
            pair.first.map { it.digitToInt() }.sumOf { it * it * it } == pair.second
        }.let { nums ->
            if (nums.count() == 0) "Unlucky"
            else "${nums.joinToString(" ") { "${it.second}" }} ${nums.sumOf { it.second }} Lucky"
        }
}
*/

/*
object Cubes {
    fun isSumOfCubes(s: String): String =
        Regex("\\d{1,3}").findAll(s)
            .map { it.value.toInt() to it.value }
            .filter { pair ->
                pair.first == pair.second.map { it.digitToInt() }.sumOf { it * it * it }
            }.let { nums ->
                if (nums.none()) "Unlucky"
                else "${nums.joinToString(" ") { "${it.first}" }} ${nums.sumOf { it.first }} Lucky"
            }
}
*/

object Cubes {
    fun isSumOfCubes(s: String): String =
        Regex("\\d{1,3}").findAll(s)
            .map { it.value.toInt() to it.value }
            .filter { pair ->
                pair.first == pair.second.map { it.digitToInt() }.sumOf { it * it * it }
            }.let { nums ->
                if (nums.none()) "Unlucky"
                else "${nums.joinToString(" ") { "${it.first}" }} ${nums.sumOf { it.first }} Lucky"
            }
}
