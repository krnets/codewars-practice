import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void sampleTests() {
        assertEquals(DD.isDD(30313), true);
        assertEquals(DD.isDD(122), true);
        assertEquals(DD.isDD(664444309), true);
        assertEquals(DD.isDD(5023011), false);
        assertEquals(DD.isDD(9081231), false);
    }
}