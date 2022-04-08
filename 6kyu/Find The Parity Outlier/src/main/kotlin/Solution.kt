/*
fun find(integers: Array<Int>): Int {
    var firstOdd: Int? = null
    var firstEven: Int? = null
    var oddCount = 0
    var evenCount = 0

    integers.forEach {
        if (it % 2 == 0) {
            ++evenCount

            if (evenCount > 1 && firstOdd != null) {
                return firstOdd as Int
            } else if (oddCount > 1)
                return it
            firstEven = it

        } else {
            ++oddCount

            if (oddCount > 1 && firstEven != null) {
                return firstEven as Int
            } else if (evenCount > 1)
                return it
            firstOdd = it
        }
    }
    return integers.first()
}
*/

fun find(integers: Array<Int>): Int =
    integers.singleOrNull { it % 2 == 0 } ?: integers.single { it % 2 != 0 }

/*
fun find(integers: Array<Int>): Int {
    var (even, odd) = integers.partition { it % 2 == 0 }
    return if (even.size == 1) even.first() else odd.first()
}
*/


