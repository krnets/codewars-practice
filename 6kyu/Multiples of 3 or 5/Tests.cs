using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void Test()
    {
        Assert.AreEqual(23, Kata.Solution(10));
    }
}