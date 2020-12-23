using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class KataTests
{
    [Test]
    public static void FixedTest_aaaa()
    {
        Dictionary<char, int> d = new Dictionary<char, int>();
        d.Add('a', 4);
        Assert.AreEqual(d, Kata.Count("aaaa"));
    }

    [Test]
    public static void FixedTest_aabb()
    {
        Dictionary<char, int> d = new Dictionary<char, int>();
        d.Add('a', 2);
        d.Add('b', 2);
        Assert.AreEqual(d, Kata.Count("aabb"));
    }
}