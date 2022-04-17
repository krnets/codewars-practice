/*
fun killKthBit(n: Int, k: Int): Int {
    return n and (1 shl (k - 1)).inv()
}*/

fun killKthBit(n: Int, k: Int): Int {
    val mask = (1 shl (k - 1)).inv()
    return n and mask
}
