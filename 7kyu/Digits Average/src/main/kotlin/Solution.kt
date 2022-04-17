/*
import kotlin.math.roundToInt

fun digitsAverage(input: Int): Int {
    if (input < 10) return input

    val nextDigits = input.toString().map { it.digitToInt() }
        .zipWithNext { a, b -> ((a + b) / 2.0).roundToInt() }
        .joinToString("").toInt()

    return digitsAverage(nextDigits)
}*/

fun digitsAverage(input: Int): Int {
    if (input < 10) return input

    val nextDigits = input.toString().map { it.digitToInt() }
        .zipWithNext { a, b -> (a + b + 1) / 2 }
        .joinToString("").toInt()

    return digitsAverage(nextDigits)
}
