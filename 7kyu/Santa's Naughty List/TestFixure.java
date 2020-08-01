import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class TestFixure {
    @Test
    public void basicTest() {
        var santasList = new ArrayList<String>();
        var children = new ArrayList<String>();
        for (String s : new String[]{"Jason", "Jackson", "Jordan", "Johnny"})
            santasList.add(s);
        for (String s : new String[]{"Jason", "Jordan", "Jennifer"})
            children.add(s);
        var goodChildren = new ArrayList<String>();

        for (String s : new String[]{"Jason", "Jordan"}) {
            goodChildren.add(s);
        }
        assertEquals(goodChildren, findList.findChildren(santasList, children));
    }

    @Test
    public void sortingTest() {
        var santasList = new ArrayList<String>();
        var children = new ArrayList<String>();
        for (String s : new String[]{"Jason", "Jackson", "Johnson", "JJ"})
            santasList.add(s);
        for (String s : new String[]{"Jason", "James", "JJ"})
            children.add(s);
        var goodChildren = new ArrayList<String>();

        for (String s : new String[]{"JJ", "Jason"}) {
            goodChildren.add(s);
        }
        assertEquals(goodChildren, findList.findChildren(santasList, children));
    }

    @Test
    public void capitalizationTest() {
        var santasList = new ArrayList<String>();
        var children = new ArrayList<String>();
        for (String s : new String[]{"jASon", "JAsoN", "JaSON", "jasON"})
            santasList.add(s);
        for (String s : new String[]{"JasoN", "jASOn", "JAsoN", "jASon", "JASON"})
            children.add(s);
        var goodChildren = new ArrayList<String>();

        for (String s : new String[]{"JAsoN", "jASon"}) {
            goodChildren.add(s);
        }
        assertEquals(goodChildren, findList.findChildren(santasList, children));
    }
}