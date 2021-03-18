using NUnit.Framework;
using System.Linq;


[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(new char[] {'a'}, Kata.Loneliest("a"));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(new char[] {'g'}, Kata.Loneliest("abc d   ef  g   h i j      "));
    }

    [Test]
    public void ExampleTest3()
    {
        Assert.AreEqual(new char[] {'b'}, Kata.Loneliest("a   b   c"));
    }

    [Test]
    public void ExampleTest4()
    {
        Assert.AreEqual(new char[] {'z'}, Kata.Loneliest("  abc  d  z    f gk s "));
    }

    [Test]
    public void ExampleTest5()
    {
        Assert.AreEqual(new char[] {'b', 'c'}, Kata.Loneliest("a  b  c  de  ").OrderBy(x => x).ToArray());
    }

    [Test]
    public void ExampleTest6()
    {
        Assert.AreEqual(new char[] {'a', 'b', 'c'}, Kata.Loneliest("abc").OrderBy(x => x).ToArray());
    }
}