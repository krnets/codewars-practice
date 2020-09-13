import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;


public class KataTest {

    @Test
    public void ShouldBeTrue() {
        assertEquals(true, Kata.SubstringTest("Millennium", "Tonne"));
        assertEquals(true, Kata.SubstringTest("Something", "Home"));
        assertEquals(true, Kata.SubstringTest("Sapiens", "Pie"));
    }

    @Test
    public void ShouldBeFalse() {
        assertEquals(false, Kata.SubstringTest("Something", "Fun"));
    }
}