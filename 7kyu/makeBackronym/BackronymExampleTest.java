import org.junit.Test;

import java.util.*;
import static junit.framework.TestCase.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

public class BackronymExampleTest {
    @Test
    public void testExample() {
        assertThat(
                Backronym.makeBackronym("dgm"),
                is("disturbing gregarious mustache"));
        assertThat(
                Backronym.makeBackronym("lkj"),
                is("literal klingon joke"));
        assertThat(
                Backronym.makeBackronym("interesting"),
                is("ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious"));
        assertThat(
                Backronym.makeBackronym("codewars"),
                is("confident oscillating disturbing eager weird awesome rant stylish"));
    }
}