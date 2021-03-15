using NUnit.Framework;
using System.Linq;

[TestFixture]
class Tests
{
    [TestCase("2 10", "2 15", 1)]
    [TestCase("2 10", "3 10", 1)]
    [TestCase("2 10", "2 10", 0)]
    [TestCase("3 9", "5 6", -1)]
    [TestCase("7 7", "5 8", -1)]
    public void BasicTests(string a, string b, int expected)
    {
        var one = Foo(a);
        var two = Foo(b);
        Assert.That(Kata.ComparePowers(one, two), Is.EqualTo(expected));
    }

    int[] Foo(string s) => s.Split().Select(int.Parse).ToArray();
}