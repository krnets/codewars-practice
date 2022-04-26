import kotlin.test.Test
import kotlin.test.assertEquals

class BasicTests {
    @Test
    fun basicTests() {
        assertEquals(listOf(15), beggars(listOf(1, 2, 3, 4, 5), 1))
        assertEquals(listOf(9, 6), beggars(listOf(1, 2, 3, 4, 5), 2))
        assertEquals(listOf(5, 7, 3), beggars(listOf(1, 2, 3, 4, 5), 3))
        assertEquals(listOf(1, 2, 3, 4, 5, 0), beggars(listOf(1, 2, 3, 4, 5), 6))
        assertEquals(listOf(), beggars(listOf(1, 2, 3, 4, 5), 0))
    }
}