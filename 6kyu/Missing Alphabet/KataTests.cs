using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTest()
    {
        Assert.AreEqual("hIJKMNPQRSTUVWXYZeFGIJKMNPQRSTUVWXYZlMNPQRSTUVWXYZloPQRSTUVWXYZ",
            MissingAlphabet.InsertMissingLetters("hello"));
    }
}