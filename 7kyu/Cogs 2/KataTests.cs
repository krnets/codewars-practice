using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    private const double delta = 1e-9;

    [Test]
    public void testBasic()
    {
        double[] expected = new[] {-1.0 / 2, -2.0};
        var actual = Cogs.CogRpm(new[] {100, 50, 25}, 1);
        Assert.AreEqual(actual.Length, 2);
        Assert.AreEqual(actual[0], expected[0], delta);
        Assert.AreEqual(actual[1], expected[1], delta);
    }
}