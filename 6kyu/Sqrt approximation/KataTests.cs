using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(2, Kata.SqrtApproximation(4), "Should work for integer roots.");
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new int[] {2, 3}, Kata.SqrtApproximation(5), "Should work for range approximation.");
    }
}