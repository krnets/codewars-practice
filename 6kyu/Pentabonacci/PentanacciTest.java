import static org.junit.Assert.*;

import org.junit.Test;


public class PentanacciTest {

    private static int randInt(int min, int max) {
        return min + (int) (Math.random() * ((max - min) + 1));
    }

    private static void testing(long actual, long expected) {
        assertEquals(expected, actual);
    }

    @Test
    public void test1() {
        System.out.println("Fixed Tests: countOddPentaFib, low values");
        long[] lstI = new long[]{45, 68, 76, 100, 121};
        long[] resultsI = new long[]{15, 23, 25, 33, 40};
        for (int i = 0; i <= 4; i++) {
            testing(Pentanacci.countOddPentaFib(lstI[i]), resultsI[i]);
        }
    }

    @Test
    public void test2() {
        System.out.println("Fixed Tests: countOddPentaFib, moderate values");
        long[] lstII = new long[]{1508, 2100, 3500, 4200, 7600, 8555, 9100, 9999};
        long[] resultsII = new long[]{503, 699, 1167, 1399, 2533, 2851, 3033, 3333};
        for (int i = 0; i <= 7; i++) {
            testing(Pentanacci.countOddPentaFib(lstII[i]), resultsII[i]);
        }
    }

    @Test
    public void test3() {
        System.out.println("Fixed Tests: countOddPentaFib, higher values");
        long[] lstIII = new long[]{13000, 15000, 16500, 17000, 18500, 20000, 25000, 32000, 34000, 37000, 40000, 44000};
        long[] resultsIII = new long[]{4333, 4999, 5499, 5667, 6167, 6667, 8333, 10667, 11333, 12333, 13333, 14667};
        for (int i = 0; i <= 11; i++) {
            testing(Pentanacci.countOddPentaFib(lstIII[i]), resultsIII[i]);
        }
    }

    //----------------------------
    private static long countOddPentaFibSol(long n) {
        return (long) ((n - 1) / 6) + (long) ((n - 2) / 6) + 1;
    }

    //----------------------------
    @Test
    public void test4() {
        System.out.println("Random Tests");
        for (int i = 0; i < 100; i++) {
            int n = randInt(1000, 10000);
            testing(Pentanacci.countOddPentaFib(n), countOddPentaFibSol(n));

        }
    }


}
