using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.That(Kata.GroupByCommas(1), Is.EqualTo("1"));
        Assert.That(Kata.GroupByCommas(12), Is.EqualTo("12"));
        Assert.That(Kata.GroupByCommas(123), Is.EqualTo("123"));
        Assert.That(Kata.GroupByCommas(1234), Is.EqualTo("1,234"));
        Assert.That(Kata.GroupByCommas(12345), Is.EqualTo("12,345"));
        Assert.That(Kata.GroupByCommas(123456), Is.EqualTo("123,456"));
        Assert.That(Kata.GroupByCommas(1234567), Is.EqualTo("1,234,567"));
        Assert.That(Kata.GroupByCommas(12345678), Is.EqualTo("12,345,678"));
        Assert.That(Kata.GroupByCommas(123456789), Is.EqualTo("123,456,789"));
        Assert.That(Kata.GroupByCommas(1234567890), Is.EqualTo("1,234,567,890"));
    }
}