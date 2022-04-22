package solution

import org.junit.Test
import org.junit.Assert.assertArrayEquals

class SolutionTest {

    @Test
    fun `one year`() {
        assertArrayEquals(arrayOf(1, 15, 15), calculateYears(1));
    }

    @Test
    fun `two years`() {
        assertArrayEquals(arrayOf(2, 24, 24), calculateYears(2));
    }

    @Test
    fun `ten years`() {
        assertArrayEquals(arrayOf(10, 56, 64), calculateYears(10));
    }
}