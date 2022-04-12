class MixedSum {
    fun sum(mixed: List<Any>): Int = mixed.sumOf { it.toString().toInt() }
}