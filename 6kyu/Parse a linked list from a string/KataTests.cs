using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new Node(1, new Node(2, new Node(3))), Kata.Parse("1 -> 2 -> 3 -> null"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual(new Node(0, new Node(1, new Node(4, new Node(9, new Node(16))))),
            Kata.Parse("0 -> 1 -> 4 -> 9 -> 16 -> null"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual(null, Kata.Parse("null"));
    }
}