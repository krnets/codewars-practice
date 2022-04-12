fun countPositivesSumNegatives(input: Array<Int>?): Array<Int> {
    if (input.isNullOrEmpty())
        return emptyArray()

    var (positives, negatives) = input!!.partition { it > 0 }

    return arrayOf(positives.count(), negatives.sum())
}