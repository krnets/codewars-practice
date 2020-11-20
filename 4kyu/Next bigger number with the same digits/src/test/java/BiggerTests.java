import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BiggerTests {

    @Test
    public void biggerTest1() {
        assertEquals(123456798, Kata.nextBiggerNumber(123456789));
    }

    @Test
    public void biggerTest2() {
        assertEquals(1234567908, Kata.nextBiggerNumber(1234567890));
    }

    @Test
    public void biggerTest3() {
        assertEquals(-1, Kata.nextBiggerNumber(9876543210L));
    }

    @Test
    public void biggerTest4() {
        assertEquals(-1, Kata.nextBiggerNumber(9999999999L));
    }

    @Test
    public void biggerTest5() {
        assertEquals(59884848483559L, Kata.nextBiggerNumber(59884848459853L));
    }

    @Test
    public void biggerTest6() {
        assertEquals(98829009, Kata.nextBiggerNumber(98820990));
    }
}
