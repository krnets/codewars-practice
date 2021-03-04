using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTests()
    {
        Assert.AreEqual("OK", Solution.solve("abba"));
        Assert.AreEqual("remove one", Solution.solve("abbaa"));
        Assert.AreEqual("not possible", Solution.solve("abbaab"));
        Assert.AreEqual("remove one", Solution.solve("madmam"));
        Assert.AreEqual("not possible", Solution.solve("raydarm"));
        Assert.AreEqual("OK", Solution.solve("hannah"));
    }
}