import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest{
    @Test
    public void basicTests(){
        assertEquals(true,Solution.solve("abc"));
        assertEquals(false,Solution.solve("aac"));
        assertEquals(false,Solution.solve("abd"));
        assertEquals(true,Solution.solve("dabc"));
        assertEquals(false,Solution.solve("abbc"));
        assertEquals(true,Solution.solve("v"));
    }
}