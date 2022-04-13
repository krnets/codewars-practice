package easyline

import org.junit.Assert.*
import java.math.BigInteger
import org.junit.Test

class EasylineTest {
    private fun testing(actual: BigInteger, expected: BigInteger) {
        assertEquals(expected, actual)
    }

    @Test
    fun test1() {
        testing(easyLine(0), BigInteger("1"))
        testing(easyLine(1), BigInteger("2"))
        testing(easyLine(4), BigInteger("70"))
        testing(easyLine(7), BigInteger("3432"))
        testing(easyLine(13), BigInteger("10400600"))
        testing(easyLine(50), BigInteger("100891344545564193334812497256"))
    }

}
