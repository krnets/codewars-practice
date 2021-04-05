using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new List<string> {"a"}, Kata.Anagrams("a", new List<string> {"a", "b", "c", "d"}));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new List<string> {"carer", "arcre", "carre"},
            Kata.Anagrams("racer",
                new List<string> {"carer", "arcre", "carre", "racrs", "racers", "arceer", "raccer", "carrer", "cerarr"}));
    }
}