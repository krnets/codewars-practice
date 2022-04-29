package solution

import kotlin.math.roundToInt

object OrdersSummary {
    fun balanceStatements(lst: String): String {
        var bought = 0.0
        var sold = 0.0
        val typos = mutableListOf<String>()
        val pattern = Regex("""^\S+ (\d+) (\d+\.\d+) (B|S)$""")

        lst.split(", ")
            .forEach {
                if (pattern.matches(it)) {
                    val (qty, pricePoint, action) = pattern.find(it)!!.destructured
                    if (action == "B") {
                        bought += qty.toDouble() * pricePoint.toDouble()
                    } else sold += qty.toDouble() * pricePoint.toDouble()
                } else
                    typos.add("$it ;")
            }

        val result = "Buy: ${bought.roundToInt()} Sell: ${sold.roundToInt()}"

        return when {
            typos.isEmpty() or lst.isEmpty() -> result
            else -> "$result; Badly formed ${typos.size}: ${typos.joinToString("")}"
        }
    }
}