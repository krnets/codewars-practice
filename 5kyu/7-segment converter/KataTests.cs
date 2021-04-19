using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void Test4()
    {
        Assert.AreEqual(0b101_1010, Kata.SevenSegmentNumber(4));
    }

    [Test]
    public void Test8()
    {
        Assert.AreEqual(0b111_1111, Kata.SevenSegmentNumber(8));
    }
}