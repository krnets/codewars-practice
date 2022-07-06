package solution

import org.junit.jupiter.api.Test
import kotlin.test.*
import java.text.DecimalFormat
import kotlin.math.abs

class SuiteTest {

    private fun assertFuzzy(n: Int, exp: Double) {
        val act = Suite.going(n)
        val inrange = abs(act - exp) <= 1e-6

        if (!inrange) {
            val df = DecimalFormat("\"#.000000\"")
            println("At 1e-6: Expected must be " + df.format(exp) + ", but got " + df.format(act))
        }
        assertEquals(true, inrange)
    }

    @Test
    fun basicTest() {
        assertFuzzy(5, 1.275)
        assertFuzzy(6, 1.2125)
        assertFuzzy(7, 1.173214)
    }
}