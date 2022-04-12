object EqualSidesOfAnArray {
    fun findEvenIndex(arr: IntArray): Int {
        var leftSum = 0
        var rightSum = arr.sum()

        arr.forEachIndexed { index, x ->
            leftSum += x

            if (leftSum == rightSum) return index

            rightSum -= x
        }

        return -1
    }
}