using NUnit.Framework;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SplitAndAdd()
    {
        int[] expected = new int[] {5, 10};
        int[] input = Kata.SplitAndAdd(new int[] {1, 2, 3, 4, 5}, 2);

        Assert.AreEqual(expected, input);

        expected = new[] {10, 18};
        input = Kata.SplitAndAdd(new[] {4, 2, 5, 3, 2, 5, 7}, 2);

        Assert.AreEqual(expected, input);

        expected = new int[] {15};
        input = Kata.SplitAndAdd(new int[] {1, 2, 3, 4, 5}, 3);

        Assert.AreEqual(expected, input);

        expected = new int[] {15};
        input = Kata.SplitAndAdd(new int[] {15}, 3);

        Assert.AreEqual(expected, input);

        expected = new int[] {183, 125};
        input = Kata.SplitAndAdd(new int[] {32, 45, 43, 23, 54, 23, 54, 34}, 2);

        Assert.AreEqual(expected, input);

        expected = new int[] {32, 45, 43, 23, 54, 23, 54, 34};
        input = Kata.SplitAndAdd(new int[] {32, 45, 43, 23, 54, 23, 54, 34}, 0);

        Assert.AreEqual(expected, input);

        expected = new int[] {305, 1195};
        input = Kata.SplitAndAdd(new int[] {3, 234, 25, 345, 45, 34, 234, 235, 345}, 3);

        Assert.AreEqual(expected, input);

        expected = new int[] {1040, 7712};
        input = Kata.SplitAndAdd(
            new int[] {3, 234, 25, 345, 45, 34, 234, 235, 345, 34, 534, 45, 645, 645, 645, 4656, 45, 3}, 4);

        Assert.AreEqual(expected, input);

        expected = new int[] {79327};
        input = Kata.SplitAndAdd(new int[] {23, 345, 345, 345, 34536, 567, 568, 6, 34536, 54, 7546, 456}, 20);

        Assert.AreEqual(expected, input);
    }
}