/*


public class AreSameTest {

    @Test
    public void test1() {
        int[] a = new int[]{121, 144, 19, 161, 19, 144, 19, 11};
        int[] b = new int[]{121, 14641, 20736, 361, 25921, 361, 20736, 361};
        assertEquals(true, AreSame.comp(a, b));

    }

}
*/

import static org.junit.Assert.*;

import org.junit.Test;

public class AreSameTest {
    @Test
    public void sample() {
        assertFalse(AreSame.comp(new int[]{121, 144, 19, 161, 19, 144, 19, 11}, null));
        assertFalse(AreSame.comp(null, null));
        assertFalse(AreSame.comp(null, new int[]{121, 144, 19, 161, 19, 144, 19, 11}));
        assertTrue(AreSame
                .comp(new int[]{121, 144, 19, 161, 19, 144, 19, 11}, new int[]{121, 14641, 20736, 361, 25921, 361, 20736, 361}));
        assertFalse(AreSame
                .comp(new int[]{121, 144, 19, 161, 19, 144, 19, 11}, new int[]{121, 14641, 20736, 361, 25921, 361, 20736}));
    }
}
