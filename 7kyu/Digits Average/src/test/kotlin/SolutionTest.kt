import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun testFixed() {
        assertEquals(4, digitsAverage(246))
        assertEquals(9, digitsAverage(89))
        assertEquals(2, digitsAverage(2))
        assertEquals(4, digitsAverage(245))
        assertEquals(5, digitsAverage(345))
        assertEquals(5, digitsAverage(346))
    }
}

