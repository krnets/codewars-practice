import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void testHello() {
        assertEquals(
                "Hello",
                Solution.binaryToText("0100100001100101011011000110110001101111"));
    }

    @Test
    public void testEmptyString() {
        assertEquals(
                "",
                Solution.binaryToText(""));
    }
}