import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun testFixed() {
        assertEquals(10, growingPlant(100, 10, 910))
        assertEquals(1, growingPlant(10, 9, 4))
    }
}