package reducebutgrow

import org.junit.Assert.assertEquals
import org.junit.Test

class ReduceButGrowTests {

    @Test
    fun exampleTests() {
        assertEquals(6, grow(intArrayOf(1, 2, 3)))
        assertEquals(16, grow(intArrayOf(4, 1, 1, 1, 4)))
        assertEquals(64, grow(intArrayOf(2, 2, 2, 2, 2, 2)))
    }
}