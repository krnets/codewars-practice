using NUnit.Framework;

[TestFixture]
public class SplitStringTests
{
    [Test]
    public void BasicTest1()
    {
        Assert.AreEqual(new[] {"ab", "c_"}, SplitString.Solution("abc"));
    }

    [Test]
    public void BasicTest2()
    {
        Assert.AreEqual(new[] {"ab", "cd", "ef"}, SplitString.Solution("abcdef"));
    }

    [Test]
    public void ExtendedTest1()
    {
        var pairs = SplitString.Solution("cdabefg");

        Assert.IsNotNull(pairs, "solution did not return a value");
        Assert.AreEqual(4, pairs.Length, "solution did not return an array with enough pairs");
        Assert.AreEqual("cd", pairs[0], "solution did not return pairs with correct values");
        Assert.AreEqual("g_", pairs[3], "solution did not return pairs with correct values");
    }

    [Test]
    public void ExtendedTest2()
    {
        var pairs = SplitString.Solution("abcd");

        Assert.IsNotNull(pairs, "solution did not return a value");
        Assert.AreEqual(2, pairs.Length, "solution did not return an array with correct number of pairs");
        Assert.AreEqual("cd", pairs[1], "last pair in solution is not correct");
    }
}