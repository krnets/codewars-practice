using System.Linq;
using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual(new Node(3, new Node(2, new Node(1, null))),
            Kata.ReverseList(new Node(1, new Node(2, new Node(3, null)))));
    }

    [Test]
    public void SampleTest2()
    {
        // For simplicity, Node can also be constructed using any non-empty IEnumerable<int>:
        Assert.AreEqual(new Node(new int[] {5, 4, 3, 2, 1}), Kata.ReverseList(new Node(new int[] {1, 2, 3, 4, 5})));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual(new Node(1), Kata.ReverseList(new Node(1)));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual(new Node(Enumerable.Range(1, 1_000_000).Reverse().ToList()),
            Kata.ReverseList(new Node((Enumerable.Range(1, 1_000_000).ToList()))));
    }
}