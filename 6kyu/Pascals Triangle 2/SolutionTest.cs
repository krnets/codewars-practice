using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void ExampleTest1()
    {
        Assert.AreEqual(new[] {new long[] {1}},
            Kata.Pascal(1));

        Assert.AreEqual(new[]
        {
            new long[] {1},
            new long[] {1, 1},
            new long[] {1, 2, 1},
            new long[] {1, 3, 3, 1},
            new long[] {1, 4, 6, 4, 1}
        }, Kata.Pascal(5));
    }

    [Test]
    public void ExampleTest2()
    {
        Assert.AreEqual(new[]
        {
            new long[] {1},
            new long[] {1, 1},
            new long[] {1, 2, 1},
            new long[] {1, 3, 3, 1},
            new long[] {1, 4, 6, 4, 1},
            new long[] {1, 5, 10, 10, 5, 1},
            new long[] {1, 6, 15, 20, 15, 6, 1},
            new long[] {1, 7, 21, 35, 35, 21, 7, 1},
            new long[] {1, 8, 28, 56, 70, 56, 28, 8, 1},
            new long[] {1, 9, 36, 84, 126, 126, 84, 36, 9, 1}
        }, Kata.Pascal(10));
    }
}