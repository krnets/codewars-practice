package romannumerals

/*
fun decode(str: String): Int {
    val fromRomanMap = mapOf(
        "M" to 1000, "CM" to 900, "D" to 500, "CD" to 400, "C" to 100, "XC" to 90,
        "L" to 50, "XL" to 40, "X" to 10, "IX" to 9, "V" to 5, "IV" to 4, "I" to 1
    )
    var ans = 0
    var i = 0

    while (i < str.length) {
        var sub = str.drop(i).take(2)
        if (fromRomanMap.containsKey(sub)) {
            ans += fromRomanMap[sub]!!
            i += 2
        } else {
            ans += fromRomanMap[str.drop(i).take(1)]!!
            i++
        }
    }
    return ans
}*/

/*
fun decode(str: String): Int {
    val roman = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
    var ans = 0
    for (i in str.indices) {
        val curr = roman[str[i]]!!
        if (i + 1 < str.length && curr < roman[str[i + 1]]!!)
            ans -= curr
        else ans += curr
    }
    return ans
}
*/

/*
fun decode(str: String): Int {
    val roman = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
    var ans = 0

    str.forEachIndexed { i, c ->
        val x = roman[c]!!
        if (i + 1 < str.length && x < roman[str[i + 1]]!!)
            ans -= x
        else ans += x
    }
    return ans
}
*/

val roman = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)

fun decode(str: String): Int = str.foldIndexed(0) { i, acc, c ->
    val x = roman[c]!!
    if (i + 1 < str.length && x < roman[str[i + 1]]!!)
        acc - x
    else acc + x
}
