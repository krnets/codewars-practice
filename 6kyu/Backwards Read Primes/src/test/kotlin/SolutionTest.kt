package backwards

import org.junit.Assert.*
import org.junit.Test

class BackWardsPrimeTest {
    @Test
    fun backWardsPrime1() {
        assertEquals("7027 7043 7057", backwardsPrime(7000, 7100))
    }

    @Test
    fun backWardsPrime2() {
        assertEquals("70001 70009 70061 70079 70121 70141 70163 70241", backwardsPrime(70000, 70245))
    }

}