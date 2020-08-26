import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

public class Tests {
    @Test public void HashTest1()
    {
        Null n=new Null();
        assertEquals(0,n.hashCode());
    }
    @Test public void HashTest2()
    {
        Null n=new Null();
        assertEquals(new Null().hashCode(), n.hashCode());
    }
    @Test
    public void Test1()
    {
        Null n=new Null();
        assertEquals(n,null);
    }
    @Test
    public void Test2()
    {
        Null n=new Null();
        assertEquals(n, n);
    }
    @Test
    public void Test3()
    {
        Null n=new Null();
        assertEquals(n, new Null());
    }
    @Test
    public void Test4()
    {
        Null n=new Null();
        assertNotEquals(new Object(),n);
    }
    @Test
    public void Test5()
    {
        Null n=new Null();
        assertEquals("null",n.toString());
    }
}