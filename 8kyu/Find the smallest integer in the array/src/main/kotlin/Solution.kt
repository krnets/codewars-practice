package solution

class SmallestIntegerFinder {
    fun findSmallestInt(nums: List<Int>): Int = nums.minOf { it }
}