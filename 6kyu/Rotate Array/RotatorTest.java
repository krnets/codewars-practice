import static org.junit.Assert.*;

import org.junit.*;

public class RotatorTest {
    private Rotator rotator;

    @Before
    public void setUp() {
        this.rotator = new Rotator();
    }

    @After
    public void tearDown() {
        this.rotator = null;
    }

    @Test
    public void testSingleRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{5, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 1));
    }

    @Test
    public void testSingleRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{2, 3, 4, 5, 1},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -1));
    }

    @Test
    public void testDoubleRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{4, 5, 1, 2, 3},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 2));
    }

    @Test
    public void testDoubleRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{3, 4, 5, 1, 2},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -2));
    }

    @Test
    public void testTripleRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{3, 4, 5, 1, 2},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 3));
    }

    @Test
    public void testTripleRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{4, 5, 1, 2, 3},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -3));
    }

    @Test
    public void testQuadRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{2, 3, 4, 5, 1},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 4));
    }

    @Test
    public void testQuadRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{5, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -4));
    }

    @Test
    public void testQuinRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{1, 2, 3, 4, 5},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 5));
    }

    @Test
    public void testQuinRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{1, 2, 3, 4, 5},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -5));
    }

    @Test
    public void testHexaRotation_ArrayOfFive_Positive() {
        assertArrayEquals(new Object[]{5, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 6));
    }

    @Test
    public void testHexaRotation_ArrayOfFive_Negative() {
        assertArrayEquals(new Object[]{2, 3, 4, 5, 1},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, -6));
    }

    @Test
    public void testDoubleRotation_ArrayOfSix_Positive() {
        assertArrayEquals(new Object[]{5, 6, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5, 6}, 2));
    }

    @Test
    public void testDoubleRotation_ArrayOfSix_Negative() {
        assertArrayEquals(new Object[]{3, 4, 5, 6, 1, 2},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5, 6}, -2));
    }

    @Test
    public void testTripleRotation_ArrayOfSeven_Positive() {
        assertArrayEquals(new Object[]{5, 6, 7, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5, 6, 7}, 3));
    }

    @Test
    public void testTripleRotation_ArrayOfSeven_Negative() {
        assertArrayEquals(new Object[]{4, 5, 6, 7, 1, 2, 3},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5, 6, 7}, -3));
    }

    @Test
    public void testZeroRotate_ArrayOfSeven() {
        assertArrayEquals(new Object[]{1, 2, 3, 4, 5, 6, 7},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5, 6, 7}, 0));
    }

    @Test
    public void testDoubleRotate_CharArray() {
        assertArrayEquals(new Object[]{'b', 'c', 'a'},
                rotator.rotate(new Object[]{'a', 'b', 'c'}, 2));
    }

    @Test
    public void testDoubleRotate_DoubleArray() {
        assertArrayEquals(new Object[]{2.0, 3.0, 1.0},
                rotator.rotate(new Object[]{1.0, 2.0, 3.0}, 2));
    }

    @Test
    public void testDoubleRotate_BooleanArray() {
        assertArrayEquals(new Object[]{true, false, true},
                rotator.rotate(new Object[]{true, true, false}, 2));
    }

    @Test
    public void testSevenRotate_ArrayOfFive() {
        assertArrayEquals(new Object[]{4, 5, 1, 2, 3},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 7));
    }

    @Test
    public void testElevenRotate_ArrayOfFive() {
        assertArrayEquals(new Object[]{5, 1, 2, 3, 4},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 11));
    }

    @Test
    public void testLargeRotate_ArrayOfFive() {
        assertArrayEquals(new Object[]{3, 4, 5, 1, 2},
                rotator.rotate(new Object[]{1, 2, 3, 4, 5}, 12478));
    }
}

