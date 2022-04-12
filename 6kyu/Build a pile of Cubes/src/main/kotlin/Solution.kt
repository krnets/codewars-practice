/*
package solution

object ASum {
    fun findNb(m: Long): Long {
        var cubeLevelSum: Long = 0
        var level: Long = 1

        while (cubeLevelSum < m) {
            cubeLevelSum += (level * level * level)
            ++level
        }
        return if (cubeLevelSum == m) level - 1 else -1
    }
}*/

package solution

object ASum {
    fun findNb(m: Long): Long {
        var cubeLevelSum = 0L

        return generateSequence(1L) { it + 1 }
            .onEach { cubeLevelSum += it * it * it }
            .takeWhile { cubeLevelSum <= m }
            .lastOrNull { cubeLevelSum == m }
            ?: -1
    }
}
