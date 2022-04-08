import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun test1() {
        assertEquals("42 -9", highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
    }
    @Test
    fun test2() {
        assertEquals("3 1", highAndLow("1 2 3"))
    }
}
