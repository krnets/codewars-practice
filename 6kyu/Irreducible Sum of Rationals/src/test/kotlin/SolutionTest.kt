package solution

import org.junit.Test
import kotlin.test.assertEquals

class SumFractionsTest {

    fun testing(actual: String, expected: String) {
        assertEquals(expected, actual)
    }

    @Test
    fun basicTests() {
        var a = arrayOf(intArrayOf(1, 2), intArrayOf(2, 9), intArrayOf(3, 18), intArrayOf(4, 24), intArrayOf(6, 48))
        var r: String = "[85, 72]"
        testing(SumFractions.sumFracts(a), r)

        a = arrayOf(intArrayOf(1, 2), intArrayOf(1, 3), intArrayOf(1, 4))
        r = "[13, 12]"
        testing(SumFractions.sumFracts(a), r)

        a = arrayOf()
        r = ""
        testing(SumFractions.sumFracts(a), r)
    }
}