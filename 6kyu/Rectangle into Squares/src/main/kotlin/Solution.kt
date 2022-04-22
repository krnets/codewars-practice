package squares

/*
fun sqInRect(length: Int, width: Int): List<Int>? {
    if (length == width) return null

    val list = mutableListOf<Int>()
    var l = length
    var w = width

    while (l * w > 0) {
        if (l > w) {
            list.add(l - (l - w))
            l -= w
        } else {
            list.add(w - (w - l))
            w -= l
        }
    }
    return list
}
*/

fun sqInRect(length: Int, width: Int): List<Int>? {
    val large = length.coerceAtLeast(width)
    val small = length.coerceAtMost(width)

    return if (large == small) null
    else listOf(small) + (sqInRect(small, large - small) ?: listOf(small))
}
