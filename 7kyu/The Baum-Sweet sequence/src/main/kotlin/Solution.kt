fun baumSweet(): Iterator<Int> = iterator {
    yield(1)
    (1..1_000_000).forEach { n ->
        n.toString(2)
            .split('1')
            .any { it.length % 2 == 1 }
            .let {
                yield(if (it) 0 else 1)
            }
    }
}