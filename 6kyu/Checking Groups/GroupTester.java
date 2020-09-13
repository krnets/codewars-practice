import org.junit.Test;

import static org.junit.Assert.*;

public class GroupTester {

    @Test
    public void testCorrectGroups() {
        assertTrue("That group was matched correctly", Groups.groupCheck("({})"));
        assertTrue("That group was matched correctly", Groups.groupCheck("[[]()]"));
        assertTrue("That group was matched correctly", Groups.groupCheck("[{()}]"));
        assertTrue("That group was matched correctly", Groups.groupCheck("()"));
        assertTrue("That group was matched correctly", Groups.groupCheck("([])"));
        assertTrue("That group was matched correctly", Groups.groupCheck("{}([])"));
        assertTrue("That group was matched correctly", Groups
                .groupCheck("{[{}[]()[]{}{}{}{}{}{}()()()()()()()()]{{{[[[((()))]]]}}}}(())[[]]{{}}[][][][][][][]({[]})"));
        assertTrue("That group was matched correctly", Groups.groupCheck(""));
    }

    @Test
    public void testBadlyMatchedGroups() {
        assertFalse("That group was matched incorrectly", Groups.groupCheck("{(})"));
        assertFalse("That group was matched incorrectly", Groups.groupCheck("[{}{}())"));
        assertFalse("That group was matched incorrectly", Groups.groupCheck("{)[}"));
        assertFalse("That group was matched incorrectly", Groups.groupCheck("[[[]])"));
        assertFalse("That group was matched incorrectly", Groups.groupCheck("()[]{]"));
        assertFalse("That group was matched incorrectly", Groups.groupCheck("{([]})"));
    }

    @Test
    public void testOpenOrPrematurelyClosedGroups() {
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("([]"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("[])"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("([]))"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("{{))"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("{}{"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("{"));
        assertFalse("That group was left open or prematurely closed", Groups.groupCheck("]"));
        assertFalse("That group was left open or prematurely closed", Groups
                .groupCheck("{{{{{{{{{{{((((((([])))))))}}}}}}}}}}"));
    }
}