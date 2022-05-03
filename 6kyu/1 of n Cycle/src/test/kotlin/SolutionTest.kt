package cycle

import org.junit.Test
import kotlin.test.assertEquals

class CycleTest {
    private fun dotest(n: Int, expected: Int) {
        val actual = cycle(n)
        assertEquals(expected.toLong(), actual.toLong())
    }

    @Test
    fun `no cycle test`() {
        dotest(5, -1)
        dotest(18118, -1)
        dotest(94, -1)
    }

    @Test
    fun `cycle found test`() {
        dotest(3, 1)
        dotest(13, 6) // 0.076923 076923 0769
        dotest(21, 6)//  0.047619 047619 0476
        dotest(27, 3)// 0.037 037 037 037 0370
        dotest(33, 2) // 0.03 03 03 03 03 03 03 03
        dotest(37, 3) // 0.027 027 027 027 027 0
        dotest(280921, 70230)
    }
}
