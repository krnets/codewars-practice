import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MaxSequenceTest {
    @Test
    public void testEmptyArray() throws Exception {
        assertEquals(0, Max.sequence(new int[]{}), "Empty arrays should have a max of 0");
    }

    @Test
    public void testExampleArray() throws Exception {
        assertEquals(6, Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}), "Example array should have a max of 6");
    }
}