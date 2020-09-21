import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals(256, Kata.nextHigher(128));
        assertEquals(2, Kata.nextHigher(1));
        assertEquals(1279, Kata.nextHigher(1022));
        assertEquals(191, Kata.nextHigher(127));
        assertEquals(1253359, Kata.nextHigher(1253343));
    }

    private int sol(int n) {
        int o = n & -n;
        return n + o | ((n ^ n + o) / o >> 2);
    }

    @Test
    public void randomTests() {
        Random r = new Random();
        int m = (1 << 30) - 1;
        for (int i = 0; i < 100; i++) {
            int n = r.nextInt(m) + 1;
            assertEquals(sol(n), Kata.nextHigher(n));
        }
    }
}
