using NUnit.Framework;
using System.Collections.Generic;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void BasicTests()
    {
        Assert.AreEqual(null, Kata.Map<string, string>(null, x => x));

        TestMap(Kata.Map(new Node<int>(1, new Node<int>(2, new Node<int>(3))), n => n),
            new Node<int>(1, new Node<int>(2, new Node<int>(3))));
    }

    [Test]
    public void MoreTests()
    {
        TestMap(Kata.Map(new Node<int>(1, new Node<int>(2, new Node<int>(3))), x => x + 3),
            new Node<int>(4, new Node<int>(5, new Node<int>(6))));

        TestMap(Kata.Map(new Node<int>(1, new Node<int>(2, new Node<int>(3))), x => x > 1),
            new Node<bool>(false, new Node<bool>(true, new Node<bool>(true))));

        TestMap(Kata.Map(new Node<string>("aaa", new Node<string>("b", new Node<string>("abc"))), x => x + 'x'),
            new Node<string>("aaax", new Node<string>("bx", new Node<string>("abcx"))));
    }

    private static void TestMap<T>(Node<T> result, Node<T> expected)
    {
        CollectionAssert.AreEqual(ToList(expected), ToList(result));
    }

    private static List<Node<T>> ToList<T>(Node<T> head)
    {
        List<Node<T>> list = new List<Node<T>>();
        Node<T> next = head;

        while (next != null)
        {
            list.Add(next);
            next = next.next;
        }

        return list;
    }
}