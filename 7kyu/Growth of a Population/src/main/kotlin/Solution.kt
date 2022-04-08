package growth

/*
fun nbYear(pp0: Int, percent: Double, aug: Int, p: Int): Int {

    val pp1 = pp0 + (pp0 * (percent / 100) + aug).toInt()

    return if (pp1 >= p) 1 else 1 + nbYear(pp1, percent, aug, p)
}*/

fun nbYear(pp0: Int, percent: Double, aug: Int, p: Int): Int =
    generateSequence(pp0) { (it + (it * percent / 100) + aug).toInt() }
        .indexOfFirst { it >= p }
