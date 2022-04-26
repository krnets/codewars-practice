/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    val arr = IntArray(n)

    arr.indices.forEach { i ->
        var x = 0
        var j = i

        while (j < values.size) {
            x += values[j]
            j += n
        }
        arr[i] = x
    }
    return arr.toList()
}*/

/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    val list = mutableListOf<Int>()

    (0 until n).forEach {
        var x = 0
        var j = it

        while (j < values.size) {
            x += values[j]
            j += n
        }
        list.add(x)
    }
    return list
}
*/

/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    val list = mutableListOf<Int>()

    (0 until n).forEach {
        var x = 0
        var j = it

        while (j < values.size) {
            x += values[j]
            j += n
        }
        list.add(x)
    }
    return list
}
*/

/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    val list = mutableListOf<Int>()

    for (i in 0 until n) {
        var sum = 0

        for (j in i until values.size step n)
            sum += values[j]

        list.add(sum)
    }
    return list
}
*/

/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    if (n == 0) return listOf()

    val arr = IntArray(n)

    for (i in values.indices)
        arr[i % n] += values[i]

    return arr.toList()
}
*/

/*
fun beggars(values: List<Int>, n: Int): List<Int> {
    return (0 until n)
        .map { values.drop(it) }
        .map { frame ->
            frame.windowed(1, n)
                .sumOf { it.first() }
        }
}
*/

fun beggars(values: List<Int>, n: Int): List<Int> = (0 until n)
    .map { values.slice(it..values.lastIndex step n).sum() }
