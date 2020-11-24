import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SimpleTests {

    @Test
    public void smallTest1() {
        assertEquals(21, Kata.nextBiggerNumber(12));
    }

    @Test
    public void smallTest2() {
        assertEquals(531, Kata.nextBiggerNumber(513));
    }

    @Test
    public void smallTest3() {
        assertEquals(2071, Kata.nextBiggerNumber(2017));
    }

    @Test
    public void smallTest4() {
        assertEquals(441, Kata.nextBiggerNumber(414));
    }

    @Test
    public void smallTest5() {
        assertEquals(414, Kata.nextBiggerNumber(144));
    }

    @Test
    public void smallTest6() {
        assertEquals(19009, Kata.nextBiggerNumber(10990));
    }
}
