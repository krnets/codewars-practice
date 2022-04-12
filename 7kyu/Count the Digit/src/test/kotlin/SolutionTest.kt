package countdig

import org.junit.Assert.assertEquals
import org.junit.Test

class CountDigTest {
    private fun testing(actual:Int, expected:Int) {
        assertEquals(expected.toLong(), actual.toLong())
    }
    @Test
    fun test() {
        println("Fixed Tests nbDig")
        testing(nbDig(5750, 0), 4700)
        testing(nbDig(11011, 2), 9481)

    }
}