import org.junit.Assert.*;
import org.junit.Test

class TestExample {
    @Test
    fun testFixed() {
        val a2 = arrayOf<String>("lively", "alive", "harp", "sharp", "armstrong")

        assertArrayEquals(arrayOf<String>("live", "strong"), inArray(arrayOf<String>("xyz", "live", "strong"), a2))
        assertArrayEquals(
            arrayOf<String>("arp", "live", "strong"),
            inArray(arrayOf<String>("live", "strong", "arp"), a2)
        )
        assertArrayEquals(arrayOf<String>(), inArray(arrayOf<String>("tarp", "mice", "bull"), a2))
    }
}
