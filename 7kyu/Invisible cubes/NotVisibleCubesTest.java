import org.junit.Assert;
import org.junit.Test;

public class NotVisibleCubesTest {
    @Test
    public void fixedTest() {
        NotVisibleCubes kata = new NotVisibleCubes();
        Assert.assertEquals("should work for 3", kata.notVisibleCubes(3L), Long.valueOf(1L));
        Assert.assertEquals("should work for 5", kata.notVisibleCubes(5L), Long.valueOf(27L));
    }
}
