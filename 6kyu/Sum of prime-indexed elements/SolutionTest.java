import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

import java.util.Random;

public class SolutionTest {
    private static Random random = new Random();

    public static int nm9(int[] arr) {
        int c = 0;
        for (int i = 2; i < arr.length; ++i)
            if (isPrime_(i)) c += arr[i];
        return c;
    }

    private static boolean isPrime_(int n) {
        for (int i = 2; i * i < n + 1; i++)
            if (n % i == 0) return false;
        return true;
    }

    private static int random(int l, int u) {
        return random.nextInt(u - l) + l;
    }

    @Test
    public void basicTests() {
        assertEquals(0, Solution.solve(new int[]{}));
        assertEquals(7, Solution.solve(new int[]{1, 2, 3, 4}));
        assertEquals(13, Solution.solve(new int[]{1, 2, 3, 4, 5, 6}));
        assertEquals(47, Solution.solve(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}));
    }

    @Test
    public void randomTests() {
        for (int i = 0; i < 100; i++) {
            int len = random(1000, 5000);
            int[] arr = new int[len];
            for (int j = 0; j < len; ++j) {
                arr[j] = random(0, 1000);
            }
            int exp = nm9(arr);
            assertEquals(exp, Solution.solve(arr));
        }
    }
}