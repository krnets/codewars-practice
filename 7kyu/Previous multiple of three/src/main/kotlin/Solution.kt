/*
fun prevMultOfThree(n: Int): Int? {
    var m = n

    while (m > 1) {
        if (m % 3 == 0)
            return m
        m /= 10
    }
    return null
}
*/

fun prevMultOfThree(n: Int): Int? = when {
    n % 3 == 0 -> n
    n < 10 -> null
    else -> prevMultOfThree(n / 10)
}

/*
fun prevMultOfThree(n: Int): Int? = generateSequence(n) { it / 10 }
    .find { it % 3 == 0 }
    .let { if (it == 0) null else it }
*/
