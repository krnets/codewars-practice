using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class KataTest
{
    [Test]
    public static void SampleTest001()
    {
        var arr = new int[] {1, 2, 3, 4};
        var cr = new int[] {2, 1, 4, 3};
        var l = ToLinkedList(arr);
        var res = FromLinkedList(Kata.KReverse(l, 2));

        // Assert.IsTrue(cr.SequenceEqual(res));
        Assert.AreEqual(cr, res);
    }

    [Test]
    public static void SampleTest002()
    {
        var arr = new int[] {1, 2, 3, 4, 5, 6};
        var cr = new int[] {3, 2, 1, 6, 5, 4};
        var l = ToLinkedList(arr);
        var res = FromLinkedList(Kata.KReverse(l, 3));

        // Assert.IsTrue(cr.SequenceEqual(res));
        Assert.AreEqual(cr, res);
    }

    private static LinkedListNode<T> ToLinkedList<T>(T[] arr)
    {
        var start = default(LinkedListNode<T>);
        var node = default(LinkedListNode<T>);

        foreach (var elem in arr)
        {
            if (node == null)
            {
                node = new LinkedListNode<T>(elem);
                start = node;
            }
            else
            {
                var next = new LinkedListNode<T>(elem);
                node.Next = next;
                node = node.Next;
            }
        }

        return start;
    }

    private static T[] FromLinkedList<T>(LinkedListNode<T> start)
    {
        var res = new List<T>();
        var n = start;

        while (n != null)
        {
            res.Add(n.Value);
            n = n.Next;
        }

        return res.ToArray();
    }
}