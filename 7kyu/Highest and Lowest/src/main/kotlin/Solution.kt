fun highAndLow(numbers: String): String {
    var list = numbers.split(" ").map { it.toInt() }
    var high = list.maxOrNull()
    var low = list.minOrNull()

    return "$high $low"
}