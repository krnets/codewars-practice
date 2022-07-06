package kprimes

import org.junit.jupiter.api.Test
import kotlin.test.*

class KPrimesTest {

    @Test
    fun test1() {
        val expected = longArrayOf(
            4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49,
            51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95
        )
        assertContentEquals(expected, countKprimes(2, 0, 100))
    }

    @Test
    fun test2() {
        val expected = longArrayOf(
            8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99
        )
        assertContentEquals(expected, countKprimes(3, 0, 100))
    }

    @Test
    fun test3() {
        val expected = longArrayOf(500, 520, 552, 567, 588, 592, 594)
        assertContentEquals(expected, countKprimes(5, 500, 600))
    }

    @Test
    fun test4() {
        assertEquals(1, puzzle(138))
    }

    @Test
    fun test5() {
        assertEquals(2, puzzle(143))
    }
}
