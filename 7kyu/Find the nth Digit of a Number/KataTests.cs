using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(5, Kata.FindDigit(5673, 4));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(2, Kata.FindDigit(129, 2));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(8, Kata.FindDigit(-2825, 3));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(0, Kata.FindDigit(-456, 4));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual(0, Kata.FindDigit(0, 20));
    }

    [Test]
    public void SampleTest6()
    {
        Assert.AreEqual(-1, Kata.FindDigit(65, 0));
    }

    [Test]
    public void SampleTest7()
    {
        Assert.AreEqual(-1, Kata.FindDigit(24, -8));
    }
}