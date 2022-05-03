/*
fun nextHigher(n: Int): Int {
    val nCountBits = n.countOneBits()

    return generateSequence(n + 1) { it + 1 }
        .first {
            it.countOneBits() == nCountBits
        }
}*/

fun nextHigher(n: Int): Int {
    val a = n and -n
    val b = (n + a) xor n
    val c = b / a
    val d = c shr 2

    return (n + a) or d
}
