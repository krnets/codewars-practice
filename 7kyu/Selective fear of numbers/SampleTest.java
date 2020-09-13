import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SampleTest {
    @Test
    public void fixedTests() {
        doTest("Monday", 13, false);
        doTest("Sunday", -666, true);
        doTest("Tuesday", 2, false);
        doTest("Tuesday", 965, true);
        doTest("Friday", 2, true);
    }

    private void doTest(final String day, final int num, final boolean expected) {
        assertEquals("Should return " + expected,
                expected, Arithmophobia.AmIAfraid(day, num));
    }
}