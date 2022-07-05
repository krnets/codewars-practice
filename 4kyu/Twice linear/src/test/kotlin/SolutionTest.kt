package dbllinear

import kotlin.test.*
import org.junit.jupiter.api.Test

class dblLinearMainTest {
    @Test
    fun test() {
        println("Fixed Tests dblLinear")
        testing(dblLinear(10), 22)
        testing(dblLinear(20), 57)
        testing(dblLinear(30), 91)

    }

    companion object {
        private fun testing(actual: Int, expected: Int) {
            assertEquals(expected.toLong(), actual.toLong())
        }
    }
}


