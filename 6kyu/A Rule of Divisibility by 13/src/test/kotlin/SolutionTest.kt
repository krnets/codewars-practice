package thirteen

import org.junit.Assert.*
import org.junit.Test

class ThirteenTest {
    @Test
    fun test1() {
        println("Fixed Tests: thirt")
        testing(thirt(8529), 79)
        testing(thirt(85299258), 31)

    }

    companion object {
        private fun testing(actual: Long, expected: Long) {
            assertEquals(expected, actual)
        }
    }
}