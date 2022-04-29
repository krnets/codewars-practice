package decod

import org.junit.Test
import kotlin.test.assertEquals

class decodTest {
    fun testingDecode(r: String, expected: String) {
        val actual: String = decode(r)
        assertEquals(expected, actual)
    }

    @Test
    fun test() {
        testingDecode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx")
        testingDecode("105860ymmgegeeiwaigsqkcaeguicc", "Impossible to decode")
        testingDecode("2460721mlptwabtlnnymizdkvfwlpwufhdsx", "evfpqajpvnnieurbmhtqvfqytlbgz")
        testingDecode("1877138eieaqgumigywmicwgcgg", "Impossible to decode")

    }
}