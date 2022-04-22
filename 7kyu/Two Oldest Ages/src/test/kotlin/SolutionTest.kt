package solution

import org.junit.Test
import kotlin.test.assertEquals

class TestTwoOldestAges {
    @Test
    fun basicTests() {
        assertEquals(listOf(45, 87), twoOldestAges(listOf(1, 5, 87, 45, 8, 8)))
        assertEquals(listOf(18, 83), twoOldestAges(listOf(6, 5, 83, 5, 3, 18)))
    }
}