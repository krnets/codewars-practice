fun babyCount(x: String): Int? {
    val charFreqMap = x.lowercase().groupingBy { it }.eachCount()

    val ans = minOf((charFreqMap['b'] ?: 0) / 2, charFreqMap['a'] ?: 0, charFreqMap['y'] ?: 0)

    return if (ans == 0) null else ans
}