package step

import org.junit.Assert.*
import org.junit.Test

class StepInPrimesTest {
    @Test
    fun `fixed tests`() {
        println("Fixed Tests")
        assertEquals("[101, 103]", step(2, 100, 110).contentToString())
        assertEquals("[103, 107]", step(4, 100, 110).contentToString())
        assertEquals("[101, 107]", step(6, 100, 110).contentToString())
        assertEquals("[2, 3]", step(1, 2, 3).contentToString())

        assertEquals("[]", step(11, 30000, 100000).contentToString())
    }

    @Test
    fun `extra tests`() {
        println("Extra Tests")

        assertEquals("[101, 107]", step(6, 100, 110).contentToString())
        assertEquals("[359, 367]", step(8, 300, 400).contentToString())
        assertEquals("[307, 317]", step(10, 300, 400).contentToString())
    }
}

