using NUnit.Framework;

[TestFixture]
public class IntroToArtTest
{
    [Test]
    public void BasicTests()
    {
        IntroToArt obj = new IntroToArt();
        // Assert.AreEqual(new string[] { }, obj.GetW(1));
        Assert.AreEqual(new string[]
        {
            "*   *   *",
            " * * * * ",
            "  *   *  "
        }, obj.GetW(3));
        Assert.AreEqual(new string[]
        {
            "*           *           *",
            " *         * *         * ",
            "  *       *   *       *  ",
            "   *     *     *     *   ",
            "    *   *       *   *    ",
            "     * *         * *     ",
            "      *           *      "
        }, obj.GetW(7));
    }
}