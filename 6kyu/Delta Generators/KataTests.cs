using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

internal class AssertHelper
{
    internal static void Assert(IList<int> expected, IList<int> actual, int n)
    {
        var msg = new StringBuilder();
        msg.AppendLine($"n: {n}");
        msg.AppendLine($"  expected: {{{string.Join(", ", expected)}}}");
        msg.AppendLine($"  actual: {{{string.Join(", ", actual)}}}");
        CollectionAssert.AreEqual(expected, actual, msg.ToString());
    }
}

// Sample Test Cases

[TestFixture(Description = "Example Tests")]
public class ExampleTestSuite
{
    internal static void Act(IList<int> expected, IEnumerable<int> enumerable, int n,
        Func<IEnumerable<int>, IList<int>> collector = null)
    {
        collector = collector ?? new Func<IEnumerable<int>, IList<int>>((xs) => xs.ToList());
        var actual = collector(Kata.Delta(enumerable, n));
        AssertHelper.Assert(expected, actual, n);
    }

    [Test(Description = "Finite Sequences")]
    public void FixedTestsFiniteSequences()
    {
        Act(new[] {1, 1, 1, 1, 1}, new[] {1, 2, 3, 4, 5, 6}, 1);
        Act(new[] {-8, 90}, new[] {3, 3, -5, 77}, 2);
        Act(new[] {0}, Enumerable.Repeat(2, 10), 9);
        Act(new[] {-8}, new[] {1, -1, 1, -1}, 3);
    }

    [Test(Description = "Infinite Sequences")]
    public void FixedTestsInfiniteSequences()
    {
        IEnumerable<int> Ones()
        {
            while (true) yield return 1;
        }

        Act(Enumerable.Repeat(0, 1000).ToList(), Ones(), 1, xs => xs.Take(1000).ToList());
        Act(Enumerable.Repeat(0, 1000).ToList(), Ones(), 100, xs => xs.Take(1000).ToList());

        IEnumerable<int> Up()
        {
            int a = 0, b = 1;
            while (true)
            {
                yield return a;
                (a, b) = (a + b, b + 3);
            }
        }

        Act(new[] {1, 4, 7, 10, 13, 16, 19, 22, 25, 28}, Up(), 1, xs => xs.Take(10).ToList());
        Act(Enumerable.Repeat(3, 10).ToList(), Up(), 2, xs => xs.Take(10).ToList());
    }
}