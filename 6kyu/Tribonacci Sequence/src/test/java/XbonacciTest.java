import org.junit.Test;
import org.junit.Before;
import org.junit.After;

import static org.junit.Assert.*;

public class XbonacciTest {

    private Xbonacci variabonacci;

    @Before
    public void setUp() throws Exception {
        variabonacci = new Xbonacci();
    }

    @After
    public void tearDown() throws Exception {
        variabonacci = null;
    }

    private double precision = 1e-10;

    @Test
    public void sampleTests() {
        assertArrayEquals(new double[]{1, 1, 1, 3, 5, 9, 17, 31, 57, 105}, variabonacci
                .tribonacci(new double[]{1, 1, 1}, 10), precision);
        assertArrayEquals(new double[]{0, 0, 1, 1, 2, 4, 7, 13, 24, 44}, variabonacci
                .tribonacci(new double[]{0, 0, 1}, 10), precision);
        assertArrayEquals(new double[]{0, 1, 1, 2, 4, 7, 13, 24, 44, 81}, variabonacci
                .tribonacci(new double[]{0, 1, 1}, 10), precision);
    }

    @Test
    public void basicTests() {
        assertArrayEquals(new double[]{1, 1, 1, 3, 5, 9, 17, 31, 57, 105}, variabonacci.tribonacci(new double[]{1, 1, 1}, 10), precision);
        assertArrayEquals(new double[]{0, 0, 1, 1, 2, 4, 7, 13, 24, 44}, variabonacci.tribonacci(new double[]{0, 0, 1}, 10), precision);
        assertArrayEquals(new double[]{0, 1, 1, 2, 4, 7, 13, 24, 44, 81}, variabonacci.tribonacci(new double[]{0, 1, 1}, 10), precision);
        assertArrayEquals(new double[]{1, 0, 0, 1, 1, 2, 4, 7, 13, 24}, variabonacci.tribonacci(new double[]{1, 0, 0}, 10), precision);
        assertArrayEquals(new double[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, variabonacci.tribonacci(new double[]{0, 0, 0}, 10), precision);
        assertArrayEquals(new double[]{1, 2, 3, 6, 11, 20, 37, 68, 125, 230}, variabonacci.tribonacci(new double[]{1, 2, 3}, 10), precision);
        assertArrayEquals(new double[]{3, 2, 1, 6, 9, 16, 31, 56, 103, 190}, variabonacci.tribonacci(new double[]{3, 2, 1}, 10), precision);
        assertArrayEquals(new double[]{1}, variabonacci.tribonacci(new double[]{1, 1, 1}, 1), precision);
        assertArrayEquals(new double[]{}, variabonacci.tribonacci(new double[]{300, 200, 100}, 0), precision);
        assertArrayEquals(new double[]{0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5}, variabonacci.tribonacci(new double[]{0.5, 0.5, 0.5}, 30), precision);

    }
}
