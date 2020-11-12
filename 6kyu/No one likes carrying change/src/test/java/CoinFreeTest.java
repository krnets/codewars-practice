import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import static org.junit.Assert.assertEquals;


public class CoinFreeTest {

    private int[] coins1 = {1, 5, 10, 25};
    private int[] coins2 = {1, 2, 5, 10, 20, 50};

    @Test
    public void test1() {
        assertEquals("75 is 25+25+25", 3, CoinFree.solve(75, coins1));
    }

    @Test
    public void test2() {
        assertEquals("123 is 25+25+25+25+10+10+1+1", 9, CoinFree.solve(123, coins1));
    }

    @Test
    public void test3() {
        assertEquals("75 is 50+20+5", 3, CoinFree.solve(75, coins2));
    }

    @Test
    public void test4() {
        assertEquals("123 is 50+50+20+2+1", 5, CoinFree.solve(123, coins2));
    }

//    @Test
//    public void test5() {
//        assertEquals(2, CoinFree.solve(10, new int[]{1, 5, 7}));
//
//    }

    @Test
    public void testUS() {
        List<int[]> tests = new ArrayList<int[]>();

        tests.add(new int[]{1, 1});
        tests.add(new int[]{10, 1});
        tests.add(new int[]{25, 1});
        tests.add(new int[]{50, 2});
        tests.add(new int[]{73, 7});
        tests.add(new int[]{125, 5});
        tests.add(new int[]{100, 4});
        int[] denom = {1, 5, 10, 25};

        for (int[] test : tests) {
            int solution = CoinFree.solve(test[0], Arrays.copyOf(denom, denom.length));
            assertEquals("Testing for " + test[0] + " cents.", test[1], solution);
        }
    }

    @Test
    public void testRichAmericans() {
        List<int[]> tests = new ArrayList<int[]>();

        tests.add(new int[]{12312, 495});
        tests.add(new int[]{34576, 1384});
        tests.add(new int[]{129671, 5189});
        tests.add(new int[]{12372, 498});
        tests.add(new int[]{120201, 4809});

        int[] denom = {1, 5, 10, 25};

        for (int[] test : tests) {
            int solution = CoinFree.solve(test[0], Arrays.copyOf(denom, denom.length));
            assertEquals("Testing for " + test[0] + " cents.", test[1], solution);
        }
    }

    @Test
    public void testStrangeCurrency() {
        List<int[]> tests = new ArrayList<int[]>();

        tests.add(new int[]{1, 1});
        tests.add(new int[]{10, 2});
        tests.add(new int[]{25, 5});
        tests.add(new int[]{50, 6});
        tests.add(new int[]{73, 7});
        tests.add(new int[]{125, 7});
        tests.add(new int[]{100, 8});

        int[] denom = {1, 3, 7, 27};

        for (int[] test : tests) {
            int solution = CoinFree.solve(test[0], Arrays.copyOf(denom, denom.length));
            assertEquals("Testing for " + test[0] + " cents.", test[1], solution);
        }
    }

    @Test
    public void testRichStrangers() {
        List<int[]> tests = new ArrayList<int[]>();

        tests.add(new int[]{1232, 48});
        tests.add(new int[]{346, 16});
        tests.add(new int[]{1291, 51});
        tests.add(new int[]{1232, 48});
        tests.add(new int[]{1201, 47});

        int[] denom = {1, 3, 7, 27};

        for (int[] test : tests) {
            int solution = CoinFree.solve(test[0], Arrays.copyOf(denom, denom.length));
            assertEquals("Testing for " + test[0] + " cents.", test[1], solution);
        }
    }

    @Test
    public void testUnorderedBases() {
        List<int[]> tests = new ArrayList<int[]>();

        tests.add(new int[]{1232, 48});
        tests.add(new int[]{346, 16});
        tests.add(new int[]{1232, 48});

        int[] b = {1, 3, 7, 27};

        for (int[] test : tests) {

            for (int i = 0; i < b.length; i++) {
                int j = rnd.nextInt(b.length);
                int tmp = b[j];
                b[j] = b[i];
                b[i] = tmp;
            }
            int solution = CoinFree.solve(test[0], Arrays.copyOf(b, b.length));
            assertEquals("Testing for " + test[0] + " cents.", test[1], solution);
        }
    }

    // Random tests
    private int getCount(int amount, int[] coinAmounts) {
        int count = 0;
        Arrays.sort(coinAmounts);
        for (int j = coinAmounts.length - 1; j >= 0 && amount > 0; j--) {
            count += amount / coinAmounts[j];
            amount %= coinAmounts[j];
        }
        return count;
    }

    private static int[] genMoneyBase(int n) {
        int[] b = new int[rnd.nextInt(7) + 1];
        int v = 1;
        for (int i = 0; i < b.length; i++) {
            b[i] = v;
            v *= 2 + rnd.nextInt(3);
        }
        for (int i = 0; i < b.length; i++) {
            int j = rnd.nextInt(b.length);
            int tmp = b[j];
            b[j] = b[i];
            b[i] = tmp;
        }
        return b;
    }

    private static final Random rnd = new Random();

    @Test
    public void someRandomTests() {
        for (int i = 0; i < 100; i++) {
            int[] denom = genMoneyBase(7);
            int amount = rnd.nextInt(2000);
            int solution = getCount(amount, Arrays.copyOf(denom, denom.length));
            String description = "Testing for " + amount +
                    " with denominations " + Arrays.toString(denom);
            assertEquals(description, solution, CoinFree.solve(amount, denom));
        }
    }

    @Test
    public void somePerfTests() {
        int M = Integer.MAX_VALUE >> 1;
        for (int i = 0; i < 1000; i++) {
            int[] denom = genMoneyBase(10);
            int amount = rnd.nextInt(M + rnd.nextInt(M >> 1));
            int solution = getCount(amount, Arrays.copyOf(denom, denom.length));
            String description = "Testing for " + amount +
                    " with denominations " + Arrays.toString(denom);
            assertEquals(description, solution, CoinFree.solve(amount, denom));
        }
    }

}
