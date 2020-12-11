using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void OneThroughFive()
    {
        Assert.AreEqual(new[] {2, 4}, NoOddities.NoOdds(new[] {1, 2, 3, 4, 5}));
    }
}