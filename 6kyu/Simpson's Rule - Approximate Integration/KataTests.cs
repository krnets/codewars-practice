using System;
using NUnit.Framework;

[TestFixture]
public static class SimpsonIntegrationTests
{
    private static void assertFuzzyEquals(double act, double exp)
    {
        bool inrange = Math.Abs(act - exp) <= 1e-10;
        if (inrange == false)
        {
            string specifier = "#.0000000000";
            Console.WriteLine(
                "At 1e-10: Expected must be " + exp.ToString(specifier) + ", but got " + act.ToString(specifier));
        }

        Assert.AreEqual(true, inrange);
    }

    [Test]
    public static void Tests()
    {
        Console.WriteLine("Fixed Tests: Simpson");
        assertFuzzyEquals(SimpsonIntegration.Simpson(290), 1.9999999986);
        assertFuzzyEquals(SimpsonIntegration.Simpson(72), 1.9999996367);
        assertFuzzyEquals(SimpsonIntegration.Simpson(252), 1.9999999975);
        assertFuzzyEquals(SimpsonIntegration.Simpson(40), 1.9999961668);
    }
}