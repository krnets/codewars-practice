import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class SumFractionsTest {

    //.................
    private static void testing(String actual, String expected) {
        assertEquals(expected, actual);
    }

    private static int randInt(int min, int max) {
        return (int) (min + Math.random() * ((max - min) + 1));
    }

    private static int comDenomSol(int[][] l) {
        int result = l[0][1];
        for (int i = 1; i < l.length; i++) {
            result = lcm0Sol(result, l[i][1]);
        }
        return result;
    }

    private static int sumNumSol(int[][] l) {
        int lc = comDenomSol(l);
        int s = 0;
        for (int i = 0; i < l.length; i++) {
            s += l[i][0] * lc / l[i][1];
        }
        return s;
    }

    private static int gcdSol(int x, int y) {
        while (y != 0) {
            int t = x;
            x = y;
            y = t % y;
        }
        return x;
    }

    private static int lcm0Sol(int a, int b) {
        return (a * b) / gcdSol(a, b);
    }


    private static String sumFractsSol(int[][] l) {
        if (l.length == 0) return "";
        int num = sumNumSol(l);
        int den = comDenomSol(l);
        if (num % den == 0) return String.valueOf(num / den);
        int gd = gcdSol(num, den);
        return Arrays.toString(new int[]{num / gd, den / gd});
    }

    //.................
    @Test
    public void test1() {
        System.out.println("Fixed Tests sumFracts");
        int[][] a = new int[][]{{1, 2}, {2, 9}, {3, 18}, {4, 24}, {6, 48}};
        String r = "[85, 72]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{1, 2}, {1, 3}, {1, 4}};
        r = "[13, 12]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{1, 3}, {5, 3}};
        r = "2";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{12, 3}, {15, 3}};
        r = "9";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{2, 7}, {1, 3}, {1, 12}};
        r = "[59, 84]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{69, 130}, {87, 1310}, {3, 4}};
        r = "[9177, 6812]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{77, 130}, {84, 131}, {60, 80}};
        r = "[67559, 34060]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{6, 13}, {187, 1310}, {31, 41}};
        r = "[949861, 698230]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{8, 15}, {7, 111}, {4, 25}};
        r = "[2099, 2775]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{};
        r = null;
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{1, 8}, {1, 9}};
        r = "[17, 72]";
        testing(SumFractions.sumFracts(a), r);
        a = new int[][]{{2, 8}, {1, 9}};
        r = "[13, 36]";
        testing(SumFractions.sumFracts(a), r);
    }

    @Test
    public void tests_B() {
        System.out.println("Random Tests");
        for (int i = 0; i < 100; i++) {
            int a = randInt(1, 200);
            int[][] op = new int[][]{{a, a + 1}, {a, a + 2}};
            testing(SumFractions.sumFracts(op), sumFractsSol(op));
        }
    }
}
