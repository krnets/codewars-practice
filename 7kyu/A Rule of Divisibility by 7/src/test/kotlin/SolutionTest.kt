package divseven

import org.junit.Assert.*
import org.junit.Test

class DivSevenTest {

    @Test
    fun test1() {
        println("Basic Tests")
        assertArrayEquals(longArrayOf(10, 2), seven(1021))
        assertArrayEquals(longArrayOf(28, 7), seven(477557101))
        assertArrayEquals(longArrayOf(47, 7), seven(477557102))

    }
}
