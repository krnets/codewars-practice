package kata

/*
object KataSolution {
    fun distributionOf(gold: IntArray): Pair<Int, Int> {
        val arr = gold.clone()
        val sum = gold.sum()

        for (i in gold.indices.drop(1)) {
            for (j in 0 until gold.size - i) {
                arr[j] = maxOf(
                    gold[j] - arr[j + 1],
                    gold[j + i] - arr[j]
                )
            }
        }
        val a = (sum + arr.first()) / 2
        val b = sum - a
        return Pair(a, b)
    }
}*/

object KataSolution {
    fun distributionOf(gold: IntArray): Pair<Int, Int> {
        val arr = gold.clone()
        val sum = gold.sum()

        for (i in gold.indices.drop(1)) {
            for (j in 0 until gold.size - i) {
                val c = gold[j] - arr[j + 1]
                val d = gold[j + i] - arr[j]

                arr[j] = maxOf(c, d)
            }
        }
        val a = (sum + arr.first()) / 2
        val b = sum - a

        return Pair(a, b)
    }
}
