using NUnit.Framework;

[TestFixture]
public class TriangularTest
{
    [Test]
    public static void TriangularTwoShouldBeThree()
    {
        Assert.AreEqual(3, Kata.Triangular(2));
    }

    [Test]
    public static void TriangularFourShouldBeTen()
    {
        Assert.AreEqual(10, Kata.Triangular(4));
    }
}