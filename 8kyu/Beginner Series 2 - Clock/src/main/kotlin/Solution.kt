/*
fun past(h: Int, m: Int, s: Int): Int {
    return h * 60 * 60 * 1000 +
            m * 60 * 1000 +
            s * 1000
}*/

/*
fun past(h: Int, m: Int, s: Int): Int {
    return (h * 60 * 60 + m * 60 + s) * 1000
}
*/

fun past(h: Int, m: Int, s: Int): Int {
    return 1000 * (60 * (60 * h + m) + s)
}
