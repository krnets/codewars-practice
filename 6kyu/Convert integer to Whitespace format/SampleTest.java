import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SampleTest {

    @Test
    public void sample() {
        assertEquals(" \t\n", Kata.whitespaceNumber(1));
        assertEquals(" \n", Kata.whitespaceNumber(0));
        assertEquals("\t\t\n", Kata.whitespaceNumber(-1));
        assertEquals(" \t \n", Kata.whitespaceNumber(2));
        assertEquals("\t\t\t\n", Kata.whitespaceNumber(-3));
    }
}