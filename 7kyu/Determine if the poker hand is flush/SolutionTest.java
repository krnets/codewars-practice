import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void BasicTests() {

        assertEquals(true,Kata.CheckIfFlush(new String[]{"AS", "3S", "9S", "KS", "4S"}));
        assertEquals(false,Kata.CheckIfFlush(new String[]{"AD", "4S", "7H", "KC", "5S"}));
        assertEquals(false,Kata.CheckIfFlush(new String[]{"AD", "4S", "10H", "KC", "5S"}));
        assertEquals(true,Kata.CheckIfFlush(new String[]{"QD", "4D", "10D", "KD", "5D"}));
    }

}