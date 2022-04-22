package kata

/*
object KataSolution {
    fun multiplicationTable(size: Int): Array<IntArray> {
        val table = mutableListOf<IntArray>()
        val range = (1..size)

        range.forEach { row ->
            table.add(range.map { row * it }.toIntArray())
        }
        return table.toTypedArray()
    }
}*/

/*
object KataSolution {
    fun multiplicationTable(size: Int): Array<IntArray> {
        val range = (1..size)

        return range.map { row ->
            range.map { it * row }.toIntArray()
        }.toTypedArray()
    }
}
*/

/*
object KataSolution {
    fun multiplicationTable(size: Int): Array<IntArray> =
        (1..size)
            .map { row ->
                (1..size)
                    .map { col -> row * col }.toIntArray()
            }.toTypedArray()
}
*/

object KataSolution {
    fun multiplicationTable(size: Int): Array<IntArray> {
        return Array(size) { x ->
            IntArray(size) { y ->
//                (x + 1) * (y + 1)
                x.inc() * y.inc()
            }
        }
    }
}
