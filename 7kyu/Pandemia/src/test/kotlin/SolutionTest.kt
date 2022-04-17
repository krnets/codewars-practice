import org.junit.Test
import org.junit.Assert

class SampleTestCases {
    @Test
    fun sampleTests() {
        val fixed = listOf(
            Pair("01000000X000X011X0X", 73.33333333333333),
            Pair("01X000X010X011XX", 72.72727272727273),
            Pair("XXXXX", 0.0),
            Pair("00000000X00X0000", 0.0),
            Pair("0000000010", 100.0),
            Pair("000001XXXX0010X1X00010", 100.0),
            Pair("X00X000000X10X0100", 42.857142857142854)
        )

        for ((input, expected) in fixed) {
            Assert.assertEquals(expected, infected(input), 1e-6)
        }
    }
}