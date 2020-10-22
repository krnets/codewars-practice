import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;

import java.util.Random;

import static org.junit.Assert.assertThat;

public class SolutionTest {

    // Reference implementation for the random test cases
    private static class PrivateTestClass {

        public static int zeros(int n) {
            double m = n / 5.0;
            int numberOfZeros = 0;
            while (m > 1) {
                numberOfZeros += (int) m;
                m = m / 5;
            }
            return numberOfZeros;
        }
    }

    private static final int MAX_N = 1000000000;
    private static final int NUM_RANDOM_TESTS = 100;

    private final Random random = new Random();

    @Test
    public void testZeros() throws Exception {
        assertThat(Solution.zeros(0), is(0));
        assertThat(Solution.zeros(6), is(1));
        assertThat(Solution.zeros(14), is(2));
        assertThat(Solution.zeros(30), is(7));
        assertThat(Solution.zeros(100), is(24));
        assertThat(Solution.zeros(1000), is(249));
        assertThat(Solution.zeros(100000), is(24999));
        assertThat(Solution.zeros(1000000000), is(249999998));
    }

    @Test
    public void testZerosRandom() throws Exception {
        for (int i = 0; i < NUM_RANDOM_TESTS; i++) {
            int n = random.nextInt(MAX_N);
            assertThat(Solution.zeros(n), is(PrivateTestClass.zeros(n)));
        }
    }
}