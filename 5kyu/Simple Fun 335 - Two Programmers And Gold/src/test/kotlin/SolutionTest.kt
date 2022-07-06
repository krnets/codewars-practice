package kata

import org.junit.jupiter.api.Test
import kotlin.test.*

class ExampleTests {
    private fun runTest(r: IntArray, sol: Pair<Int, Int>) = assertEquals(sol, KataSolution.distributionOf(r))

    @Test
    fun `Basic Tests`() {
        runTest(intArrayOf(4, 7, 2, 9, 5, 2), Pair(18, 11))
        runTest(intArrayOf(10, 1000, 2, 1), Pair(1001, 12))
        runTest(intArrayOf(10, 1000, 2), Pair(12, 1000))
        runTest(intArrayOf(140, 649, 340, 982, 105, 86, 56, 610, 340, 879), Pair(3206, 981))

        runTest(
            intArrayOf(162, 272, 320, 90, 861, 258, 29, 507, 896, 990, 411, 480, 252, 835, 730, 289, 239, 894),
            Pair(4632, 3883)
        )
    }
}