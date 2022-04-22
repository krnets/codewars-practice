package sumofparts

/*
fun sumParts(ls: IntArray): IntArray {
    val res = IntArray(ls.size + 1)
    var sum = ls.sum()

    ls.forEachIndexed { i, x ->
        res[i] = sum
        sum -= x
    }
    return res
}*/

/*
fun sumParts(ls: IntArray): IntArray {
    val res = IntArray(ls.size + 1)

    for (i in ls.indices.reversed())
        res[i] = ls[i] + res[i + 1]

    return res
}
*/

/*
fun sumParts(ls: IntArray): IntArray {
    return ls.foldRightIndexed(IntArray(ls.size + 1)) { i, x, res ->
        res[i] = res[i + 1] + x
        res
    }
}*/

fun sumParts(ls: IntArray): IntArray {
    return IntArray(ls.size + 1).apply {
        ls.foldRightIndexed(0) { i, x, acc ->
            (acc + x).also {
                this[i] = it
            }
        }
    }
}
