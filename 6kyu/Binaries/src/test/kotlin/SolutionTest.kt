package binary

import org.junit.Test
import kotlin.test.assertEquals

class binaryTest {
    private fun testingCode(s: String, expected: String) {
        val actual: String = code(s)
        assertEquals(expected, actual)
    }

    private fun testingDecode(s: String, expected: String) {
        val actual: String = decode(s)
        assertEquals(expected, actual)
    }

    @Test
    fun test1() {
        println("Fixed Tests code")
        testingCode("62", "0011100110")
        testingCode("55337700", "001101001101011101110011110011111010")
        testingCode("1119441933000055", "1111110001100100110000110011000110010111011110101010001101001101")
        testingCode("69", "00111000011001")
        testingCode("86", "00011000001110")
    }

    @Test
    fun test2() {
        println("Fixed Tests decode")
        testingDecode("10001111", "07")
        testingDecode(
            "001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100",
            "444666333666777444"
        )
        testingDecode("01110111110001100100011000000110000011110011110111011100110000110001100110", "33198877334422")
        testingDecode(
            "0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111",
            "55500011144466666699919777777"
        )
        testingDecode(
            "01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000",
            "3331977777733322222211100019888"
        )
    }
}