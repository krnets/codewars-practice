package romannumerals

import kotlin.test.assertEquals
import org.junit.Test

class TestEncode {
    @Test
    fun basic() {
        assertEquals("", encode(0))
        assertEquals("I", encode(1))
        assertEquals("IV", encode(4))
        assertEquals("XXI", encode(21))
        assertEquals("MMVIII", encode(2008))
        assertEquals("MDCLXVI", encode(1666))
        assertEquals("MMCCCXXIV", encode(2324))
        assertEquals("DXCVII", encode(597))
    }
}
