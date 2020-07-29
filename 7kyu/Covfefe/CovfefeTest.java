import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class CovfefeTest {
    @Test
    public void basicTest() {
        assertEquals("nothing covfefe", Covfefe.covfefe("nothing"));
        assertEquals("double space  covfefe", Covfefe.covfefe("double space "));
        assertEquals("covfefe covfefe", Covfefe.covfefe("covfefe"));
        assertEquals("covfefe covfefe", Covfefe.covfefe("coverage coverage"));
        assertEquals("covfefe", Covfefe.covfefe("coverage"));
    }
}