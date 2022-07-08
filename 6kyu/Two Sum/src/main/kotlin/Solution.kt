package kata

object TwoSum {
    fun twoSum(numbers: IntArray, target: Int): Pair<Int, Int> {
        val map = mutableMapOf<Int, Int>()

        for (i in numbers.indices) {
            val complement = target - numbers[i]

            if (map.containsKey(complement)) {
                return map[complement]!! to i
            }
            map[numbers[i]] = i
        }
        return 0 to 0
    }
}