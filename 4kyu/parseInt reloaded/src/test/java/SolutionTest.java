import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void basicTest0() {
        assertEquals(0, Parser.parseInt("zero"));
    }

    @Test
    public void basicTest1() {
        assertEquals(1, Parser.parseInt("one"));
    }

    @Test
    public void basicTest20() {
        assertEquals(20, Parser.parseInt("twenty"));
    }

    @Test
    public void basicTest246() {
        assertEquals(246, Parser.parseInt("two hundred and forty-six"));
    }

    @Test
    public void basicTest783_919() {
        assertEquals(783_919, Parser.parseInt(
                "seven hundred eighty-three thousand nine hundred and nineteen"));
    }

    @Test
    public void basicTest1_000_000() {
        assertEquals(1_000_000, Parser.parseInt("one million"));
    }

    @Test
    public void fixedTests() {
        assertEquals(0, Parser.parseInt("zero"));
        assertEquals(1, Parser.parseInt("one"));
        assertEquals(2, Parser.parseInt("two"));
        assertEquals(3, Parser.parseInt("three"));
        assertEquals(4, Parser.parseInt("four"));
        assertEquals(5, Parser.parseInt("five"));
        assertEquals(6, Parser.parseInt("six"));
        assertEquals(7, Parser.parseInt("seven"));
        assertEquals(8, Parser.parseInt("eight"));
        assertEquals(9, Parser.parseInt("nine"));
        assertEquals(10, Parser.parseInt("ten"));
        assertEquals(20, Parser.parseInt("twenty"));
        assertEquals(21, Parser.parseInt("twenty-one"));
        assertEquals(37, Parser.parseInt("thirty-seven"));
        assertEquals(46, Parser.parseInt("forty-six"));
        assertEquals(59, Parser.parseInt("fifty-nine"));
        assertEquals(68, Parser.parseInt("sixty-eight"));
        assertEquals(72, Parser.parseInt("seventy-two"));
        assertEquals(83, Parser.parseInt("eighty-three"));
        assertEquals(94, Parser.parseInt("ninety-four"));
        assertEquals(100, Parser.parseInt("one hundred"));
        assertEquals(101, Parser.parseInt("one hundred one"));
        assertEquals(101, Parser.parseInt("one hundred and one"));
        assertEquals(169, Parser.parseInt("one hundred sixty-nine"));
        assertEquals(299, Parser.parseInt("two hundred and ninety-nine"));
        assertEquals(736, Parser.parseInt("seven hundred thirty-six"));
        assertEquals(2000, Parser.parseInt("two thousand"));
        assertEquals(1337, Parser.parseInt("one thousand three hundred and thirty-seven"));
        assertEquals(10000, Parser.parseInt("ten thousand"));
        assertEquals(26359, Parser.parseInt("twenty-six thousand three hundred and fifty-nine"));
        assertEquals(35000, Parser.parseInt("thirty-five thousand"));
        assertEquals(99999, Parser.parseInt("ninety-nine thousand nine hundred and ninety-nine"));
        assertEquals(666666, Parser.parseInt("six hundred sixty-six thousand six hundred sixty-six"));
        assertEquals(700000, Parser.parseInt("seven hundred thousand"));
        assertEquals(200003, Parser.parseInt("two hundred thousand three"));
        assertEquals(200003, Parser.parseInt("two hundred thousand and three"));
        assertEquals(203000, Parser.parseInt("two hundred three thousand"));
        assertEquals(500300, Parser.parseInt("five hundred thousand three hundred"));
        assertEquals(888888, Parser.parseInt("eight hundred eighty-eight thousand eight hundred and eighty-eight"));
        assertEquals(1000000, Parser.parseInt("one million"));
    }
}