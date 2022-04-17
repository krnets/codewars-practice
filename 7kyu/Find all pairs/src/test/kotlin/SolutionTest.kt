import org.junit.Test
import kotlin.test.assertEquals

class PairsTest {

    @Test
    fun simpleTests() {
        assertEquals(2, duplicates(intArrayOf(1, 2, 5, 6, 5, 2)))
        assertEquals(4, duplicates(intArrayOf(1, 2, 2, 20, 6, 20, 2, 6, 2)))
        assertEquals(3, duplicates(intArrayOf(0, 0, 0, 0, 0, 0, 0)))
        assertEquals(1, duplicates(intArrayOf(1000, 1000)))
        assertEquals(0, duplicates(intArrayOf()))
        assertEquals(0, duplicates(intArrayOf(54)))
    }
}