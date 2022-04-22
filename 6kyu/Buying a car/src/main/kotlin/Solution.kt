package solution

import kotlin.math.roundToInt

object BuyCar {
    fun nbMonths(
        startPriceOld: Int,
        startPriceNew: Int,
        savingperMonth: Int,
        percentLossByMonth: Double
    ): Pair<Int, Int> {
        var months = 0
        var moneySaved = 0

        var currentPercentLossByMonth = percentLossByMonth
        var loss = currentPercentLossByMonth / 100

        var depreciatedPriceOld = startPriceOld.toDouble()
        var depreciatedPriceNew = startPriceNew.toDouble()

        while ((depreciatedPriceOld + moneySaved) < depreciatedPriceNew) {
            depreciatedPriceOld -= (depreciatedPriceOld * loss)
            depreciatedPriceNew -= (depreciatedPriceNew * loss)

            moneySaved += savingperMonth
            months++

            if (months % 2 == 1) {
                currentPercentLossByMonth += 0.5
                loss = currentPercentLossByMonth / 100
            }
        }
        val moneyLeftOver = (moneySaved + depreciatedPriceOld - depreciatedPriceNew).roundToInt()

        return Pair(months, moneyLeftOver)
    }
}