using NUnit.Framework;

[TestFixture]
public class KataTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(true, Kata.IsBalanced("(Sensei says yes!)", "()"));
        Assert.AreEqual(false, Kata.IsBalanced("(Sensei says no!", "()"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(true, Kata.IsBalanced("(Sensei [says] yes!)", "()[]"));
        Assert.AreEqual(false, Kata.IsBalanced("(Sensei [says) no!]", "()[]"));
    }

    [Test]
    public void BasicTest3()
    {
        Assert.AreEqual(true, Kata.IsBalanced("Sensei says -yes-!", "--"));
        // Assert.AreEqual(false, Kata.IsBalanced("Sensei -says no!", "--"));
    }
}