using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual(3, Kata.CountArgs(1, 2, 3));
        Assert.AreEqual(3, Kata.CountArgs(1, 2, "uhsaf uas"));
        Assert.AreEqual(1, Kata.CountArgs(1));
        Assert.AreEqual(4, Kata.CountArgs('a', 865, "asfhgajsf", new object[] {"dawdjio", null, new List<object>()}));
        Assert.AreEqual(0, Kata.CountArgs());
    }
}