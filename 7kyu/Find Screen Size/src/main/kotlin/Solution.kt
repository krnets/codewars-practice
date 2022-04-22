/*
fun findScreenHeight(width: Int, ratio: String): String {
    val (x, y) = ratio.split(':').map { it.toDouble() }
    val height = (width / (x / y)).toInt()
    return "${width}x$height"
}*/

fun findScreenHeight(width: Int, ratio: String): String {
    val (w, h) = ratio.split(':').map { it.toInt() }
    val height = (width * h / w)
    return "${width}x$height"
}
