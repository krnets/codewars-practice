import kotlin.test.assertEquals
import org.junit.Test

class TestReplace {

    @Test
    fun testFixed() {
        assertEquals("H!!", replace("Hi!"));
        assertEquals("!H!! H!!", replace("!Hi! Hi!"));
        assertEquals("!!!!!", replace("aeiou"));
        assertEquals("!BCD!", replace("ABCDE"));
    }
}