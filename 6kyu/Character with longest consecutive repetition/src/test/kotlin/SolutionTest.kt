package kata

import org.junit.jupiter.api.Test
import kotlin.test.*

class ExampleTests {
    private fun runTest(s: String, pair: Pair<Char?, Int>) = assertEquals(pair, KataSolution.longestRepetition(s))

    @Test
    fun `Example tests`() {
        runTest("aaaabb", Pair('a', 4))
        runTest("bbbaaabaaaa", Pair('a', 4))
        runTest("cbdeuuu900", Pair('u', 3))
        runTest("abbbbb", Pair('b', 5))
        runTest("aabb", Pair('a', 2))
        runTest("", Pair(null, 0))
        runTest("ba", Pair('b', 1))
    }
}
