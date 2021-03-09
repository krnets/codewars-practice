using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual("Thisi" + "\n" + "sanex" + "\n" + "ample" + "\n" + "strin" + "\n" + "g",
            Kata.StringBreakers(5, "This is an example string"));
    }
}