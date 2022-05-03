/*
object Dinglemouse {
    fun int123(a: Int): Long = Integer.toUnsignedLong(123 - a)
}
*/

object Dinglemouse {
    fun int123(a: Int): Long =
        (123L - a).takeIf { it >= 0 } ?: Long.MAX_VALUE - a + 124
}
