import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

import java.util.*;

public class MinimumNumber {
    @Test
    public void checkSmallArraySize() {
        assertEquals(1, Solution.minimumNumber(new int[]{3, 1, 2}));
        assertEquals(0, Solution.minimumNumber(new int[]{5, 2}));
        assertEquals(0, Solution.minimumNumber(new int[]{1, 1, 1}));
    }

    @Test
    public void checkLargerArraySize() {
        assertEquals(5, Solution.minimumNumber(new int[]{2, 12, 8, 4, 6}));
        assertEquals(2, Solution.minimumNumber(new int[]{50, 39, 49, 6, 17, 28}));
    }

    @Test
    public void testRandomNumbers() {
        for (int i = 0; i < 100; i++) {
            int[] a = new int[(int) (Math.random() * 48) + 3]; // Array size range: [3, 50)
            Arrays.setAll(a, j -> (int) (Math.random() * 1001) + 1);
            assertEquals(solution(a), Solution.minimumNumber(a));
        }
    }

    private static boolean isPrime(int n) {
        if (n < 1) return false;
        if (n < 4) return true;
        if (n % 2 == 0) return false;
        for (int x = 3; x <= Math.sqrt(n); x += 2) if (n % x == 0) return false;
        return true;
    }

    private static int solution(int[] numbers) {
        int sum = Arrays.stream(numbers).sum(), x = (sum + 1) % 2;
        while (!isPrime(sum + x)) x += 2;
        return x;
    }
}