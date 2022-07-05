package mix

data class MaxCounter(val char: Char, val count: Int, val src: String)

fun mix(s1: String, s2: String): String {
    val s1lowerCount = s1.filter { it.isLetter() && it.isLowerCase() }.groupingBy { it }.eachCount()
    val s2lowerCount = s2.filter { it.isLetter() && it.isLowerCase() }.groupingBy { it }.eachCount()
    val cmp1 = Comparator<MaxCounter> { o1, o2 -> o2.count - o1.count }
    val cmp2 = Comparator<MaxCounter> { o1, o2 -> if (o1.src + o1.char > o2.src + o2.char) 1 else -1 }

    return ('a'..'z')
        .map { c ->
            val s1count = s1lowerCount.getOrDefault(c, 0)
            val s2count = s2lowerCount.getOrDefault(c, 0)
            val mx = maxOf(s1count, s2count)
            val src = if (s1count < mx) "2" else if (mx > s2count) "1" else "="
            MaxCounter(c, mx, src)
        }
        .filter { it.count > 1 }
        .sortedWith(cmp1.thenComparing(cmp2))
        .joinToString("/") {
            "${it.src}:${it.char.toString().repeat(it.count)}"
        }
}