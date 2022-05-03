fun paperFold(): Iterator<Int> = iterator {
    for (k in 1..1_000_000) {
        yield(if (k and ((k and -k) shl 1) == 0) 1 else 0)
    }
}

/*
fun paperFold(): Iterator<Int> = generateSequence(1, Int::inc)
    .map { k ->
        if (k and (Integer.lowestOneBit(k) shl 1) == 0) 1 else 0
    }.iterator()
*/

