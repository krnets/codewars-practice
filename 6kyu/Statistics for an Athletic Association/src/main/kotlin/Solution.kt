package solution

import kotlin.math.pow

/*
object Stat {
    fun stat(s: String): String {
        val runners = s.split(", ")
            .map {
                it.split("|")
                    .map { n -> n.toInt() }
                    .reversed()
                    .foldRightIndexed(0.0) { index, n, acc ->
                        acc + (n * (Math.pow(60.0, index.toDouble())))
                    }
            }.sorted()

        val n = runners.size
        val stats = runners.stream().mapToInt { it.toInt() }.summaryStatistics()
        val range = stats.max - stats.min
        val average = stats.average.toInt()
        val median = (if (n % 2 == 0) (runners[(n - 1) / 2] + runners[n / 2]) / 2.0 else runners[n / 2]).toInt()

        return "Range: ${helpFormat(range)} Average: ${helpFormat(average)} Median: ${helpFormat(median)}"
    }

    private fun helpFormat(total: Int): String = listOf(
        "%02d".format(total / 60 / 60),
        "%02d".format(total / 60 % 60),
        "%02d".format(total % 60)
    ).joinToString("|")
}*/

object Stat {
    fun stat(s: String): String {
        val runners = s.split(", ")
            .map {
                it.split("|")
                    .mapIndexed { index, n ->
                        n.toInt() * 60.0.pow(2 - index)
                    }.sum()
            }.sorted()

        val n = runners.size
        val stats = runners.stream().mapToInt { it.toInt() }.summaryStatistics()
        val range = stats.max - stats.min
        val median = (if (n % 2 == 0) (runners[(n - 1) / 2] + runners[n / 2]) / 2 else runners[n / 2]).toInt()

        fun Int.toHMS() = "%02d|%02d|%02d".format(this / 60 / 60, this / 60 % 60, this % 60)

        return "Range: ${range.toHMS()} Average: ${stats.average.toInt().toHMS()} Median: ${median.toHMS()}"
    }
}