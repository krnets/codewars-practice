using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("Thi1s is2 3a T4est", Kata.Order("is2 Thi1s T4est 3a"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("Fo1r the2 g3ood 4of th5e pe6ople", Kata.Order("4of Fo1r pe6ople g3ood th5e the2"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("", Kata.Order(""));
    }
}