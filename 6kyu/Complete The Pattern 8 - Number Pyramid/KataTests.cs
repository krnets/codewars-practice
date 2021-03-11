using NUnit.Framework;

[TestFixture]
public class NumberPyramidTests
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual("", NumberPyramid.Pattern(0));
        Assert.AreEqual("", NumberPyramid.Pattern(-25));
        Assert.AreEqual("1", NumberPyramid.Pattern(1));
        Assert.AreEqual("   1   \n  121  \n 12321 \n1234321", NumberPyramid.Pattern(4));
        Assert.AreEqual(
            "      1      \n     121     \n    12321    \n   1234321   \n  123454321  \n 12345654321 \n1234567654321",
            NumberPyramid.Pattern(7));
    }
}