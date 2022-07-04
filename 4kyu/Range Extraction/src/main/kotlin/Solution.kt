import java.util.TreeMap

/*
fun rangeExtraction(arr: IntArray): String {
    val list = mutableListOf<String>()
    var start = arr.first()
    var end = arr.first()

    for (x in arr.drop(1)) {
        if (x - end != 1) {
            if (start == end) {
                list.add("$end")
            } else {
                helper(end, start, list)
            }
            start = x
            end = x
        } else {
            end = x
        }
    }
    helper(end, start, list)

    return list.joinToString(",")
}

private fun helper(end: Int, start: Int, list: MutableList<String>) {
    if (end - start == 1) {
        list.add("$start")
        list.add("$end")
    } else
        list.add("$start-$end")
}*/


/*
fun rangeExtraction(arr: IntArray): String {
    val rangeMap = mutableMapOf<Int, Int>()
    var prevKey = arr.first()
    var preVal = prevKey
    rangeMap[prevKey] = preVal

    for (x in arr.drop(1)) {
        if (x - preVal == 1) {
            rangeMap[prevKey] = x
        } else {
            rangeMap[x] = x
            prevKey = x
        }
        preVal = x
    }

    val extraValues = mutableListOf<Int>()

    rangeMap.forEach { (k, v) ->
        if (v - k == 1) {
            rangeMap[k] = k
            extraValues.add(v)
        }
    }
    extraValues.forEach { rangeMap[it] = it }

    return rangeMap.toSortedMap().map { (k, v) ->
        if (k == v) "$k"
        else "$k-$v"
    }.joinToString(",")
}
*/

fun rangeExtraction(arr: IntArray): String {
    val rangeMap = TreeMap<Int, Int>()
    var prevKey = arr.first()
    var preVal = prevKey
    rangeMap[prevKey] = preVal

    for (x in arr.drop(1)) {
        if (x - preVal == 1) {
            rangeMap[prevKey] = x
        } else {
            rangeMap[x] = x
            prevKey = x
        }
        preVal = x
    }

    val extraValues = mutableListOf<Int>()
    rangeMap.forEach { (k, v) -> if (v - k == 1) { rangeMap[k] = k.also { extraValues.add(v) } } }
    extraValues.forEach { rangeMap[it] = it }

    return rangeMap.map { (k, v) -> if (k == v) "$k" else "$k-$v" }.joinToString(",")
}
