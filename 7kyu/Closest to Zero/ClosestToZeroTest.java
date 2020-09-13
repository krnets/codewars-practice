import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * @author Marko Bekhta
 */
public class ClosestToZeroTest {

    @Test
    public void find() throws Exception {
        assertEquals(Integer.valueOf(1), ClosestToZero.find(new int[]{10, 3, 9, 1}));
        assertEquals(Integer.valueOf(-1), ClosestToZero.find(new int[]{2, 4, -1, -3}));
        assertEquals(Integer.valueOf(0), ClosestToZero.find(new int[]{13, 0, -6}));
        assertEquals(Integer.valueOf(-2147483648), ClosestToZero.find(new int[]{-2147483648}));
    }

    @Test
    public void shouldReturnNone() throws Exception {
        assertEquals(null, ClosestToZero.find(new int[]{5, 1, -1, 2, -10}));
        assertEquals(null, ClosestToZero.find(new int[]{5, 11, 11, 2, -1, 1}));
    }

}