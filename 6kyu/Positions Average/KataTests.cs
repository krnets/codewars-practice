using System;
using NUnit.Framework;

[TestFixture]
public static class PositionAverageTests
{
    private static Random rnd = new Random();

    private static void assertFuzzy(string s, double exp)
    {
        Console.WriteLine("Testing " + s);
        bool inrange;
        double merr = 1e-9;
        double actual = PositionAverage.PosAverage(s);
        inrange = Math.Abs(actual - exp) <= merr;
        if (inrange == false)
        {
            Console.WriteLine("Expected mean must be near " + exp + ", got " + actual);
        }

        Assert.AreEqual(true, inrange);
    }

    [Test]
    public static void Test1()
    {
        Console.WriteLine("Fixed Tests");
        assertFuzzy("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096", 26.6666666667);
        assertFuzzy("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490", 29.2592592593);
        assertFuzzy("4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444", 100);
    }
}