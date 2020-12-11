using NUnit.Framework;

[TestFixture]
public class Tests
{
    [Test]
    public void CodEWaRs()
    {
        Assert.AreEqual(new[] {0, 3, 4, 6}, Kata.Capitals("CodEWaRs"));
    }

    [Test]
    public void NoneOrEmpty()
    {
        Assert.AreEqual(new int[] { }, Kata.Capitals("none"));
        Assert.AreEqual(new int[] { }, Kata.Capitals(""));
    }

    [Test]
    public void TestOther()
    {
        Assert.AreEqual(new[] {0, 1, 2, 3, 4, 5}, Kata.Capitals("ALLALL"));
        Assert.AreEqual(new[] {0}, Kata.Capitals("Kata"));
    }
}