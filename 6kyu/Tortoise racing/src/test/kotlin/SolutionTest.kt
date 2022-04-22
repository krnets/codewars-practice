package tortoise

import java.util.Arrays
import org.junit.Assert.*
import org.junit.Test

class TortoiseTest {
    @Test
    fun test1() {
        println("Basic Tests")
        assertArrayEquals(intArrayOf(0, 32, 18), race(720, 850, 70))
        assertArrayEquals(intArrayOf(3, 21, 49), race(80, 91, 37))
        assertArrayEquals(intArrayOf(), race(91, 80, 37))
    }
}