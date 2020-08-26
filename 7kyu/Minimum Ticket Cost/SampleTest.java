import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class SampleTest {
    @Test
    public void basicTests() {
        doTest(2, 0);
        doTest(10, 4);
    }

    private void doTest(final int n, final int expected) {
        assertEquals(expected, Kata.findJane(n));
    }
}