package morsecode

import org.junit.Assert.assertEquals
import org.junit.Test

class DecodeTheMorseCodeTests {
    @Test
    fun exampleTestCases() {
        assertEquals("HEY JUDE", decodeMorse(".... . -.--   .--- ..- -.. ."))
        assertEquals("E E", decodeMorse(" .   ."))
    }
}