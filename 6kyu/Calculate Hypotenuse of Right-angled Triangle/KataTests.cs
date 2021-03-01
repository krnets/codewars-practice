using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual(1.414, Kata.CalculateHypotenuse(1, 1));
        Assert.AreEqual(5.000, Kata.CalculateHypotenuse(3, 4));
        Assert.AreEqual(12.728, Kata.CalculateHypotenuse(9, 9));
    }
}