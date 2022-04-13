package solution

import kotlin.test.assertEquals
import org.junit.Test

class AtmTest {
    @Test
    fun `ATM Payment Possible`() {
        assertEquals(4, count(770))
        assertEquals(1, count(10))
    }

    @Test
    fun `ATM Payment Impossible`() {
        assertEquals(-1, count(125))
        assertEquals(-1, count(238))
    }
}