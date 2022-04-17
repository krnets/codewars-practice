package target

import java.time.LocalDate
import kotlin.math.ceil
import kotlin.math.log

/*
import java.sql.Date

fun dateNbDays(a0: Double, a: Double, p: Double): String {
    var currentAmount = a0
    var daysToReachTarget: Long = 0
    val strDate = "2016-01-01"
    val depositDate = Date.valueOf(strDate).toLocalDate()
    val interestRatePerDay = 1 + p / 100 / 360

    while (currentAmount < a) {
        currentAmount *= interestRatePerDay
        daysToReachTarget++
    }
    return depositDate.plusDays(daysToReachTarget).toString()
}*/

/*
fun dateNbDays(a0: Double, a: Double, p: Double): String {
    var currentAmount = a0
    var daysToReachTarget: Long = 0
    val strDate = "2016-01-01"
    val depositDate = LocalDate.parse(strDate)
    val interestRatePerDay = 1 + p / 100 / 360

    while (currentAmount < a) {
        currentAmount *= interestRatePerDay
        daysToReachTarget++
    }
    return depositDate.plusDays(daysToReachTarget).toString()
}
*/

/*
fun dateNbDays(a0: Double, a: Double, p: Double): String {
    val depositDate = LocalDate.parse("2016-01-01")
    val interestRatePerDay = 1 + p / 100 / 360
    val delta = log(a / a0, interestRatePerDay)
    val daysToReachTarget = ceil(delta).toLong()

    return depositDate.plusDays(daysToReachTarget).toString()
}*/

/*
fun dateNbDays(a0: Double, a: Double, p: Double): String = LocalDate.parse("2016-01-01")
    .plusDays(
        (ceil(
            log(a / a0, 1 + p / 100 / 360)
        )).toLong()
    ).toString()
*/

fun dateNbDays(a0: Double, a: Double, p: Double): String {
    return LocalDate.parse("2016-01-01")
        .plusDays(
            generateSequence(a0) {
                it + it * p / 100 / 360
            }.takeWhile { it < a }.count().toLong()
        ).toString()
}
