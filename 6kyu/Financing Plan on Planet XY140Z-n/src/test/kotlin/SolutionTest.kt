package solution

import java.math.BigInteger
import org.junit.Test
import kotlin.test.assertEquals

class FinanceTest {

    @Test
    fun basicTests() {
        assertEquals(BigInteger.valueOf(105), Finance.finance(5))
        assertEquals(BigInteger.valueOf(168), Finance.finance(6))
        assertEquals(BigInteger.valueOf(252), Finance.finance(7))
        assertEquals(BigInteger.valueOf(360), Finance.finance(8));
        assertEquals(BigInteger.valueOf(2040), Finance.finance(15));
        assertEquals(BigInteger.valueOf(62537505000), Finance.finance(5000))
    }
}