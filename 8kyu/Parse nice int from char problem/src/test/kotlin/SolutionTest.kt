package basic

import kotlin.test.assertEquals
import org.junit.Test

class TestAge {
    @Test
    fun basicTests() {
        assertEquals(4, ParseIntCharProblem().getAge("4 years old"));
        assertEquals(5, ParseIntCharProblem().getAge("5 years old"));
        assertEquals(7, ParseIntCharProblem().getAge("7 years old"));
    }
}