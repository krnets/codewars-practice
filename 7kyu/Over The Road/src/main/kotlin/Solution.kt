/* TLE although valid on small N
fun overTheRoad(address: Int, n: Int): Int {
    val (odd, even) = (1..(2 * n)).partition { it % 2 == 1 }
    val zipped = odd.zip(even.reversed())

    return if (address % 2 == 0)
        zipped[n - address / 2].first
    else zipped[address / 2].second
}*/

/*
fun overTheRoad(address: Int, n: Int): Int {
    return 2 * n - address + 1
}
*/

fun overTheRoad(address: Int, n: Int): Int = n * 2 + 1 - address
