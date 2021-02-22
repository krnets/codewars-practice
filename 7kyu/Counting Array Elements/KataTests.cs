using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest()
    {
        Assert.AreEqual(new Dictionary<string, int> {{"a", 2}, {"b", 3}},
            Kata.Count(new List<string> {"a", "b", "b", "a", "b"}));
    }
}