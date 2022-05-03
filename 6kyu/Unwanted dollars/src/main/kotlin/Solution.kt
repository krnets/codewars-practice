package com.codewars.geoffp

/*
object UnwantedDollars {
    fun moneyValue(money: String): Double = money
        .replace(Regex("[^-\\.\\d]"), "")
        .let {
            if (!it.contains(Regex("\\d"))) 0.0
            else it.toDouble()
        }
}*/

/*
object UnwantedDollars {
    fun moneyValue(money: String): Double = money
        .replace(Regex("[^-\\.\\d]"), "")
        .toDoubleOrNull() ?: 0.0
}
*/

object UnwantedDollars {
    fun moneyValue(money: String): Double = money
        .replace(Regex("[$\\s]"), "")
        .toDoubleOrNull() ?: 0.0
}
