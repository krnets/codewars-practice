package kprimessteps

import org.junit.jupiter.api.Test
import kotlin.test.*

class KprimesStepsTest {
    fun listArrayLongToString(res: List<LongArray>): String {
        var s = "["

        for (i in res.indices) {
            val a = res[i]
            s += "[${a[0]}, ${a[1]}"
            s += if (i < res.size - 1) "], " else "]"
        }
        return "$s]"
    }

    fun testing(k: Int, step: Int, start: Long, nd: Long, expected: String) {
        val a = kprimesStep(k, step, start, nd)
        val actual = listArrayLongToString(a)
        assertEquals(expected, actual)
    }

    @Test
    fun BasicTest() {
        println("Basic Tests")
        testing(10, 8, 2425364, 2425700, "[]")
        testing(6, 8, 2627371, 2627581, "[[2627408, 2627416], [2627440, 2627448], [2627496, 2627504]]")

    }
}