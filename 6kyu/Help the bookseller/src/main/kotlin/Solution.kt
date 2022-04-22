package solution

/*
object StockList {
    fun stockSummary(lstOfArt: Array<String>, lstOfCat: Array<String>): String {
        if (lstOfArt.isEmpty() or lstOfCat.isEmpty()) return ""

        val categoryMap = mutableMapOf<Char, Int>()

        lstOfArt.forEach {
            val (category, nBooks) = it.split(" ")
            categoryMap[category.first()] = nBooks.toInt() + categoryMap.getOrDefault(category.first(), 0)
        }
        return lstOfCat.joinToString(" - ") {
            "(${it.first()} : ${categoryMap.getOrDefault(it.first(), 0)})"
        }
    }
}*/

object StockList {
    fun stockSummary(lstOfArt: Array<String>, lstOfCat: Array<String>): String {
        if (lstOfArt.isEmpty() or lstOfCat.isEmpty()) return ""

        val categoryMap = mutableMapOf<String, Int>()

        lstOfCat.forEach { category ->
            categoryMap.putIfAbsent(category, 0)

            lstOfArt.forEach { art ->
                val (bookCode, n) = art.split(" ")

                if (bookCode.startsWith(category)) {
                    categoryMap.merge(category, n.toInt()) { a, b -> a + b }
                }
            }
        }
        return categoryMap.entries
            .joinToString(" - ") { "(${it.key} : ${it.value})" }
    }
}
