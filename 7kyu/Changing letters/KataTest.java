import org.junit.Test;
import java.util.Random;
import static org.junit.Assert.*;

public class KataTest {

    @Test
    public void swap_1() {
        assertEquals("HEllOWOrld!",Kata.swap("HelloWorld!"));
    }

    @Test
    public void swap_2() {
        assertEquals("SUndAy",Kata.swap("Sunday"));
    }
}


