import kotlin.test.assertEquals
import org.junit.Test

class TestWillYou {
    @Test
    fun `Basic Tests`() {
        assertEquals(false, willYou(true, true, true))
        assertEquals(true, willYou(true, false, true))
        assertEquals(false, willYou(false, false, false))
        assertEquals(true, willYou(false, false, true))
    }
}