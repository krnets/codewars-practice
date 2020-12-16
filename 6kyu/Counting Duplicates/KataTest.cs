using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public void KataTest1()
    {
        Assert.AreEqual(0, Kata.DuplicateCount(""));
    }

    [Test]
    public void KataTest2()
    {
        Assert.AreEqual(0, Kata.DuplicateCount("abcde"));
    }

    [Test]
    public void KataTest3()
    {
        Assert.AreEqual(2, Kata.DuplicateCount("aabbcde"));
    }

    [Test]
    public void KataTest4()
    {
        Assert.AreEqual(2, Kata.DuplicateCount("aabBcde"), "should ignore case");
    }

    [Test]
    public void KataTest5()
    {
        Assert.AreEqual(1, Kata.DuplicateCount("Indivisibility"));
    }

    [Test]
    public void KataTest6()
    {
        Assert.AreEqual(2, Kata.DuplicateCount("Indivisibilities"), "characters may not be adjacent");
    }
}