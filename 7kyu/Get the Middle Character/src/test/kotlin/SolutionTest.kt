package middle

import kotlin.test.assertEquals
import org.junit.Test

class MiddleTest {
    @Test
    fun basicTest() {
        assertEquals("es", getMiddle("test"));
        assertEquals("dd", getMiddle("middle"));
        assertEquals("t", getMiddle("testing"));
        assertEquals("A", getMiddle("A"));
    }
}