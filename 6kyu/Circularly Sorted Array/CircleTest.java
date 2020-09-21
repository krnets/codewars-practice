import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CircleTest {
    @Test
    public void testtrue() throws Exception {
        CircleSorted calc = new CircleSorted();

        int[] A = {2, 3, 4, 1};
        int[] B = {20, 39, 87, 0, 1,};
        int[] C = {5, 6, 54, 435, 888, 9999, -8, 1, 2};
        int[] D = {70, 1, 4, 5, 7, 54, 69};
        int[] E = {2, 3, 4, 4, 6, 6, -8, -3, 0, 1};
        int[] F = {2, 3, 4, 5, 6};
        assertEquals(true,
                calc.isCircleSorted(A));
        assertEquals(true,
                calc.isCircleSorted(B));
        assertEquals(true,
                calc.isCircleSorted(C));
        assertEquals(true,
                calc.isCircleSorted(D));
        assertEquals(true,
                calc.isCircleSorted(E));
        assertEquals(true,
                calc.isCircleSorted(F));
    }

    @Test
    public void testfalse() throws Exception {
        CircleSorted calc = new CircleSorted();
        int[] A = {2, 3, 4, 3};
        int[] B = {12, 24, 22, 27, 29, 0, 4};
        int[] C = {5, 6, 54, 435, 888, 99, -8, 1, 2};
        int[] D = {70, 1, 4, 3, 7, 54, 69};
        int[] E = {2, 3, 4, 4, 6, 6, -8, -10, 0, 1};
        assertEquals(false,
                calc.isCircleSorted(A));
        assertEquals(false,
                calc.isCircleSorted(B));
        assertEquals(false,
                calc.isCircleSorted(C));
        assertEquals(false,
                calc.isCircleSorted(D));
        assertEquals(false,
                calc.isCircleSorted(E));
    }
}
