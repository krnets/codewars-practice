using NUnit.Framework;

[TestFixture]
public class Test
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(true, Kata.IsAlt("amazon"));
        Assert.AreEqual(false, Kata.IsAlt("apple"));
        Assert.AreEqual(true, Kata.IsAlt("banana"));
    }
}