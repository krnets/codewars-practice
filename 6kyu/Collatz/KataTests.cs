using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("3->10->5->16->8->4->2->1", Kata.Collatz(3));
    }
}