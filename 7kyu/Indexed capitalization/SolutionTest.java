import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void basicTest(){
        assertEquals("aBCdeF", Solution.capitalize("abcdef", new int[]{1,2,5}));
        assertEquals("aBCdeF", Solution.capitalize("abcdef", new int[]{1,2,5,100}));
        assertEquals("cOdEwArs", Solution.capitalize("codewars", new int[]{1,3,5,50}));
        assertEquals("abRacaDabRA", Solution.capitalize("abracadabra", new int[]{2,6,9,10}));
        assertEquals("codewArriors", Solution.capitalize("codewarriors", new int[]{5}));
    }
}