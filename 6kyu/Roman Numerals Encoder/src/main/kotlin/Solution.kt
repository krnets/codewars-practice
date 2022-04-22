package romannumerals

/*
fun encode(num: Int): String {
    if (num == 0) return ""

    val toRomanMap = mapOf(
        1000 to "M", 900 to "CM", 500 to "D", 400 to "CD", 100 to "C", 90 to "XC",
        50 to "L", 40 to "XL", 10 to "X", 9 to "IX", 5 to "V", 4 to "IV", 1 to "I"
    )
 val toRomanMap = mapOf(
    1000 to "M", 900 to "CM", 500 to "D", 400 to "CD", 100 to "C", 90 to "XC",
    50 to "L", 40 to "XL", 10 to "X", 9 to "IX", 5 to "V", 4 to "IV", 1 to "I"
)   val sb = StringBuilder()
    var x = num

    toRomanMap.forEach { (k, v) ->
        if (x / k > 0) {
            sb.append(v.repeat(x / k))
            x -= (x / k * k)
        }
    }
    return sb.toString()
}*/

val toRomanMap = mapOf(
    1000 to "M", 900 to "CM", 500 to "D", 400 to "CD", 100 to "C", 90 to "XC",
    50 to "L", 40 to "XL", 10 to "X", 9 to "IX", 5 to "V", 4 to "IV", 1 to "I"
)

/*
fun encode(num: Int): String {
    for ((k, v) in toRomanMap) {
        if (num / k > 0) {
            return v.repeat(num / k) + encode(num - (num / k * k))
        }
    }
    return ""
}
*/

/*
fun encode(num: Int): String {
    toRomanMap.forEach { (k, v) ->
        if (num / k > 0)
            return v.repeat(num / k) + encode(num - (num / k * k))
    }
    return ""
}
*/

fun encode(num: Int): String {
    toRomanMap.forEach { (k, v) ->
        if (num / k > 0)
            return v.repeat(num / k) + encode(num % k)
    }
    return ""
}
