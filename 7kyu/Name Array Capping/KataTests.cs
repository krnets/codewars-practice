using NUnit.Framework;


[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual(new string[] {"Expected"}, Kata.CapMe(new string[] {"ExPeCteD"}));
    }
}