package solution

import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun sampleTestCases() {
        assertEquals("DDDaadddddff", stringExpansion("3D2a5d2f"))
        assertEquals("aaabbbccc", stringExpansion("3abc"))
        assertEquals("abcd", stringExpansion("abcd"))
    }
}