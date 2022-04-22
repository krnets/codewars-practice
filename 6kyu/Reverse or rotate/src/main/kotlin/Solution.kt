package revrot

/*
fun revRot(str: String, sz: Int): String {
    val sb = StringBuilder()

    (0..str.length - sz step sz).forEach {
        val chunk = str.drop(it).take(sz)
        val sumCubes = chunk.sumOf {
            var x = it.digitToInt()
            x * x * x
        }
        if (sumCubes % 2 == 0)
            sb.append(chunk.reversed())
        else sb.append(chunk.substring(1)).append(chunk.first())
    }
    return sb.toString()
}*/

fun revRot(str: String, sz: Int): String = str.chunked(sz)
    .filter { it.length == sz }
    .joinToString("") {
        if (it.sumOf { c -> c.digitToInt() } % 2 == 0)
            it.reversed()
        else it.drop(1) + it.first()
    }

