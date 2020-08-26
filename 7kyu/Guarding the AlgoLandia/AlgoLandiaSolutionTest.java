import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class AlgoLandiaSolutionTest {
    @Test
    public void testAlreadySafe() {
        assertEquals(0,
                AlgoLandiaSolution.findNeededGuards(new boolean[]{true, true, false, true, false}));
    }

    @Test
    public void testEasy() {
        assertEquals(2,
                AlgoLandiaSolution.findNeededGuards(new boolean[]{false, false, true, false, false}));
    }
}