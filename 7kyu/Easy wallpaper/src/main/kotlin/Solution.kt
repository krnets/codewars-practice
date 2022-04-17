package wallpaper

fun wallpaper(l: Double, w: Double, h: Double): String {
    val numbers = listOf(
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    )
    if (l * w * h == 0.0) return numbers.first()

    val rollLength = 10
    val rollWidth = 52.0
    val rollExtraPercent = 15.0

    val s = 2 * (h * (l + w))
    val extra = (100 + rollExtraPercent) / 100
    val k = s * extra / (rollWidth / rollLength) + 1

    return numbers[k.toInt()]
}