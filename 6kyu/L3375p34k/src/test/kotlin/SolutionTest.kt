package com.codewars.hybris95

import org.junit.Assert.*
import org.junit.Test

class LeetspeakTest {

    internal var myEncoder: Leetspeak = Leetspeak()

    @Test
    fun simpleTest() {
        assertTrue("empty string", myEncoder.encode("") == "")
        assertTrue("abcdef string", myEncoder.encode("abcdef") == "4bcd3f")
    }
}
