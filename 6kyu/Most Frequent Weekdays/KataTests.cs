using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(new[] {"Friday", "Saturday"}, Kata.MostFrequentDays(2016));
        Assert.AreEqual(new[] {"Monday"}, Kata.MostFrequentDays(1770));
        Assert.AreEqual(new[] {"Monday"}, Kata.MostFrequentDays(2001));
        Assert.AreEqual(new[] {"Monday", "Tuesday"}, Kata.MostFrequentDays(1968));
        Assert.AreEqual(new[] {"Saturday"}, Kata.MostFrequentDays(1785));
        Assert.AreEqual(new[] {"Saturday"}, Kata.MostFrequentDays(1910));
        Assert.AreEqual(new[] {"Saturday"}, Kata.MostFrequentDays(2135));
        Assert.AreEqual(new[] {"Sunday"}, Kata.MostFrequentDays(3043));
        Assert.AreEqual(new[] {"Sunday"}, Kata.MostFrequentDays(3150));
        Assert.AreEqual(new[] {"Thursday"}, Kata.MostFrequentDays(3361));
        Assert.AreEqual(new[] {"Tuesday"}, Kata.MostFrequentDays(1901));
        Assert.AreEqual(new[] {"Tuesday"}, Kata.MostFrequentDays(3230));
        Assert.AreEqual(new[] {"Wednesday"}, Kata.MostFrequentDays(1794));
        Assert.AreEqual(new[] {"Wednesday"}, Kata.MostFrequentDays(1986));
    }
}